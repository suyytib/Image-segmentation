# 导入Flask-SQLAlchemy的SQLAlchemy类，用于在Flask应用中集成SQLAlchemy ORM
from flask_sqlalchemy import SQLAlchemy   

# 导入Flask-Migrate的Migrate类，用于在Flask应用中集成数据库迁移功能
from flask_migrate import Migrate   

# 导入Flask-Mail的Mail 类，用于在Flask应用中集成邮件发送功能
from flask_mail import Mail   

# 创建一个SQLAlchemy实例，用于在Flask应用中定义和操作数据库模型
db = SQLAlchemy()  

# 创建一个Flask-Migrate实例，用于管理数据库迁移（如升级、降级等）
migrate = Migrate()  

# 创建一个Flask-Mail实例，用于配置和发送电子邮件
mail = Mail()

# 这些代码属于数据库配置模块，但为了防止循环导入的问题发生，单独放一个文件里