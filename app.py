from flask import Flask, render_template, request, Response, redirect, url_for, session, send_from_directory,jsonify
import sqlite3
from werkzeug.security import check_password_hash,generate_password_hash

app = Flask(__name__, template_folder='D:/project', static_folder='D:/project')
app.secret_key = 'your_secret_key'  # Required for session management
is_speaking = False

# Function to check user credentials from the database
def check_credentials(attorney_id, password):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    # Query the database for user
    cursor.execute("SELECT password FROM users WHERE attorney_id=?", (attorney_id,))
    user = cursor.fetchone()
    conn.close()
    
    # Check if user exists and password is correct
    if user and check_password_hash(user[0], password):
        return True
    return False


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        attorney_id = request.form['attorney_id']
        password = request.form['password']

        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute("SELECT password FROM users WHERE attorney_id = ?", (attorney_id,))
        result = cursor.fetchone()
        conn.close()

        if result and check_password_hash(result[0], password):
            # Valid credentials
            session['attorney_id'] = attorney_id
            return redirect('/videos1')  # or wherever your dashboard is
        else:
            # Invalid credentials
            return render_template('login.html', error="Invalid Attorney ID or Password.")
    
    return render_template('login.html', error=None)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        attorney_id = request.form['attorney_id']
        password = request.form['password']
        email = request.form['email']

        hashed_password = generate_password_hash(password)

        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO users (attorney_id, password, email) VALUES (?, ?, ?)",
                           (attorney_id, hashed_password, email))
            conn.commit()
        except sqlite3.IntegrityError:
            conn.close()
            return render_template('signup.html', error="Attorney ID already exists.")
        
        conn.close()
        return redirect('/')
    
    return render_template('signup.html', error=None)


def serve_video_with_range(file_path):
    def generate():
        with open(file_path, 'rb') as f:
            while chunk := f.read(1024*8):  # Read in 8KB chunks
                yield chunk
    
    return Response(generate(), mimetype="video/mp4")

# Route to serve videos
@app.route('/videos/<filename>')
def serve_video(filename):
    return send_from_directory('D:/project', filename)

# Route for videos page
@app.route('/videos1')
def videos1():
    if 'attorney_id' not in session:
        return redirect(url_for('login'))
    return render_template('videos1.html')

@app.route("/update_voice_status", methods=["POST"])
def update_voice_status():
    global is_speaking
    data = request.json
    is_speaking = data["speaking"]
    print(f"Speaking: {is_speaking}")  # You can log or use this info
    return jsonify({"status": "updated", "speaking": is_speaking})


@app.route('/forgot-password', methods=['GET', 'POST'])
def forgot_password():
    message = ""
    success = False

    if request.method == 'POST':
        email = request.form['email']

        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()

        # Check if email exists
        cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
        user = cursor.fetchone()

        if user:
            # Email exists → show reset link sent
            message = "Reset link sent to your email."
            success = True
        else:
            # Email does not exist → add it to DB automatically
            try:
                # Insert new user with empty attorney_id and password
                cursor.execute("INSERT INTO users (attorney_id, password, email) VALUES (?, ?, ?)",
                               ("", "", email))
                conn.commit()
                message = "Email added to database. Reset link sent."
                success = True
            except sqlite3.IntegrityError:
                message = "Error adding email to database."
                success = False

        conn.close()

    return render_template("forgot-password.html", message=message, success=success)



# Logout route
@app.route('/logout')
def logout():
    session.pop('attorney_id', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
