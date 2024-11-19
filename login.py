from flask import Flask, render_template_string, request, redirect, flash, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Secret key for session management

# Bootstrap Login Page Template
login_page = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login</title>
    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body class="bg-light d-flex align-items-center justify-content-center" style="height: 100vh; background-image: url('https://thumbs.dreamstime.com/b/gentle-nature-background-butterfly-blurred-324410107.jpg'); background-size: cover; background-position: center;">
    <div class="card shadow" style="width: 100%; max-width: 400px;">
        <div class="card-body">
            <h1 class="text-center mb-4">Login</h1>
            <form method="post" action="/login">
                <div class="mb-3">
                    <label for="username" class="form-label">Username</label>
                    <input type="text" class="form-control" id="username" name="username" placeholder="Enter your username" required>
                </div>
                <div class="mb-3">
                    <label for="password" class="form-label">Password</label>
                    <input type="password" class="form-control" id="password" name="password" placeholder="Enter your password" required>
                </div>
                <button type="submit" class="btn btn-primary w-100">Login</button>
            </form>
            {% if message %}
            <div class="alert alert-danger mt-3 text-center" role="alert">
                {{ message }}
            </div>
            {% endif %}
        </div>
    </div>
    <!-- Bootstrap JS Bundle -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
"""

# Base Template with Bootstrap
base_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ title }}</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body class="bg-light" style="background-image: url('https://e0.pxfuel.com/wallpapers/383/973/desktop-wallpaper-white-rabbit-cute-rabbit.jpg'); background-size: 100vh; background-position: center;">

    <header class="bg-primary text-white py-3">
        <div class="container d-flex justify-content-between align-items-center">
            <h1 class="h4 mb-0">Python Flask Application</h1>
            <div>
                {% if session.logged_in %}
                    <a href="/logout" class="btn btn-danger">Logout</a>
                {% else %}
                    <a href="/login" class="btn btn-success">Login</a>
                {% endif %}
            </div>
        </div>
    </header>

    <nav class="navbar navbar-expand-lg navbar-light bg-light">
        <div class="container-fluid">
            <a class="navbar-brand" href="/">Home</a>
            <div class="navbar-nav">
                <a class="nav-link" href="/contact">Contact</a>
                <a class="nav-link" href="/custom">Custom Page</a>
            </div>
        </div>
    </nav>

    <main class="container my-4">
        {% block content %}
        {% endblock %}
    </main>

   

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
"""

@app.route('/login', methods=['GET', 'POST'])
def login():
    message = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Example credentials
        if username == 'admin' and password == 'admin':
            session['logged_in'] = True  # Set session variable
            flash('Login successful!', 'success')
            return redirect('/')
        else:
            message = "Invalid username or password!"
    return render_template_string(login_page, message=message)


@app.route('/')
def home():
    return render_template_string(base_template, title="Home", content="""
        <h2>Welcome to My Python Page!</h2>
        <p>This is the homepage of our Flask app. Navigate to other pages using the links above.</p>
    """)


@app.route('/contact')
def contact():
    return render_template_string(base_template, title="Contact Us", content="""
        <h2>Contact Us</h2>
        <p>Reach out to us for inquiries or support.</p>
    """)


@app.route('/custom')
def custom():
    return render_template_string(base_template, title="Custom Page", content="""
        <h2>Custom Page</h2>
        <p>Explore our custom content here.</p>
    """)


@app.route('/logout')
def logout():
    session.pop('logged_in', None)  # Clear the session
    flash('You have been logged out.', 'info')
    return redirect('/login')


@app.route('/privacy-policy')
def privacy_policy():
    return render_template_string(base_template, title="Privacy Policy", content="""
        <h2>Privacy Policy</h2>
        <p>Learn how we handle your data responsibly.</p>
    """)


@app.route('/terms-of-service')
def terms_of_service():
    return render_template_string(base_template, title="Terms of Service", content="""
        <h2>Terms of Service</h2>
        <p>Understand the rules for using our services.</p>
    """)


@app.route('/about')
def about():
    return render_template_string(base_template, title="About Us", content="""
        <h2>About Us</h2>
        <p>Discover more about our mission and team.</p>
    """)


if __name__ == '__main__':
    app.run(debug=True)
