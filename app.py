from flask import *

app = Flask(__name__)


@app.route("/register", methods=["GET","POST"])
def register():
    if request.method=="GET":
        return render_template("register.html")
    else:
        # 1.接收到用户通过POST发送的数据
        ID = request.form.get("ID")
        password = request.form.get("password")
        gender = request.form.get("gender")
        hobit = request.form.get("hobit")
        city = request.form.get("city")
        skill_list = request.form.get("skill")
        el = request.form.get("else")
        print(ID, password, gender, hobit, city, skill_list, el)
        # 将文件写入文件或者数据库中或Excel

        # 2.返回结果
        return "注册成功"

@app.route("/login", methods=["GET","POST"])
def login():
    if request.method=="GET":

        return render_template("login.html")
    else:
        print(request.form)
        ID = request.form.get("ID")
        password = request.form.get("password")
        return "登录成功"

if __name__ == "__main__":
    app.run()
