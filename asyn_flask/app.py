from flask import Flask,render_template,request,jsonify

app = Flask(__name__)

USERS = {
    "1":{"name":"小黑","count":3},
    "2":{"name":"小白","count":2},
    "3":{"name":"小黄","count":1},
}


@app.route('/user/list')
def user_list():
    import time
    return render_template("user_list.html",users=USERS)


@app.route("/vote",methods=["POST"])
def vote():
    uid = request.form.get("uid")
    USERS[uid]["count"] += 1
    return "投票成功"


@app.route("/get/vote",methods=["GET"])
def get_vote():
    return jsonify(USERS)


if __name__ == '__main__':
    app.run()
