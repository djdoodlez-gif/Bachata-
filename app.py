from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def feed():
    return render_template('feed.html', active_page='feed')

@app.route('/music')
def music():
    return render_template('music.html', active_page='music')

@app.route('/messages')
def messages():
    return render_template('messages.html', active_page='messages')

@app.route('/profile')
def profile():
    user = {
        "name": "DJ Doodlez",
        "status": "online",
        "city": "Ростов-на-Дону",
        "bio": "Bachata • Social dance • DJ sets 🔥",
        "avatar_initials": "DD"
    }
    return render_template('profile.html', user=user, active_page='profile')

@app.route('/groups')
def groups():
    return render_template('groups.html', active_page='groups')

if __name__ == '__main__':
    app.run(debug=True)
