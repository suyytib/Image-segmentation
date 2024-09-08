from flask import Flask
from blueprints.login import bp as login_bp  
from blueprints.box import bp as box_bp  
from blueprints.wems import bp as wems_bp  
from blueprints.tieba import bp as tieba_bp  
from blueprints.deeplearning import bp as deeplearning_bp  
from blueprints.deplaning import bp as deplaning_bp  
from blueprints.imageprocessing import bp as imageprocessing_bp   
from blueprints.onlinetesting import bp as onlinetesting
from table_config import db, migrate, mail  
import config  
from flask import session  
from flask import g  
from flask import render_template  
from model import Captcha, Questions, Tiebas, User,Comment
import flask_admin as admin
from flask_admin.contrib.sqla import ModelView 
class MyV1(ModelView):
    def is_accessible(self):
        if g.user_id:
            user = User.query.get(g.user_id)
            if (user.permissions>=3):
                return True
        return False
    
class MyV2(ModelView):
    def is_accessible(self):
        if g.user_id:
            user = User.query.get(g.user_id)
            if (user.permissions>=2):
                return True
        return False
    
app = Flask(__name__)  
admin = admin.Admin(app, name='My Admin', template_mode='bootstrap3')
admin.add_view(MyV1(User, db.session))
admin.add_view(MyV2(Comment, db.session))
admin.add_view(MyV2(Captcha, db.session))
admin.add_view(MyV2(Tiebas, db.session))
admin.add_view(MyV2(Questions, db.session))

# 注册蓝图到 Flask 应用程序，使它们成为应用程序的一部分  
app.register_blueprint(login_bp)  
app.register_blueprint(box_bp)  
app.register_blueprint(tieba_bp)  
app.register_blueprint(wems_bp)  
app.register_blueprint(deplaning_bp)  
app.register_blueprint(deeplearning_bp)  
app.register_blueprint(onlinetesting) 
app.register_blueprint(imageprocessing_bp)  

# 从 config 模块加载 Flask 应用程序的配置设置  
app.config.from_object(config)  
  
# 初始化数据库连接并将其绑定到 Flask 应用程序  
db.init_app(app)  
  
# 初始化数据库迁移工具并将其绑定到 Flask 应用程序  
migrate.init_app(app, db)  
  
# 初始化邮件发送功能并将其绑定到 Flask 应用程序  
mail.init_app(app)  

# 这是一个在请求之前运行的函数，用于检查用户是否已登录  
# 如果用户已登录，它将用户的 ID 存储在 Flask 的 g 对象中，以便在请求的生命周期内使用  
@app.before_request  
def captcha_login():  
    temp = session.get("user_id")  
    """ session.clear() """
    if temp:  
        user = User.query.get(temp)  
        if user:  # 这里建议检查 user 是否真的存在，防止 ID 无效的情况  
            setattr(g, "user_id", user.id)  
    else:  
        setattr(g, "user_id", None)  

# 定义根路由（'/'），当用户访问网站的主页时，将渲染 'root.html' 模板  
@app.route('/')  
def root():  
    return render_template("root.html")  
if __name__ == '__main__':  
    # 运行 Flask 应用程序，如果 debug=True，则应用程序将在调试模式下运行，并自动重新加载代码更改  
    app.run(debug=True)