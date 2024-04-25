from app import app,handler
from flask import request,render_template,abort
from linebot.exceptions import InvalidSignatureError


@app.route("/")
def home():
    return render_template("home.html")


#接收LINE平台送來的通知
@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers["X-Line-Signature"]
    print(signature)
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    print(body)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)


    return "OK"

