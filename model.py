# 从table_config模块中导入数据库实例db  
from table_config import db

# 用户表  
class User(db.Model):  
    # 定义数据库中的表名  
    __tablename__ = "user"

    # 定义用户ID列，类型为整数，是主键且自动增长  
    id = db.Column(db.Integer, primary_key=True, autoincrement=True) 

    # 定义用户名列，类型为最大长度为10的字符串，不可为空  
    username = db.Column(db.String(10), nullable=False)

    # 定义密码列，类型为最大长度为200的字符串，不可为空  
    password = db.Column(db.String(200), nullable=False) 

    # 定义邮箱列，类型为最大长度为255的字符串，不可为空  
    email = db.Column(db.String(255), nullable=False)

    status=db.Column(db.String(255), nullable=False)

    permissions=db.Column(db.Integer, nullable=False)

class Captcha(db.Model):  
    # 定义数据库中的表名  
    __tablename__ = "captcha"

    # 定义验证码ID列，类型为整数，是主键且自动增长  
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    # 定义邮箱列，类型为最大长度为255的字符串，不可为空  
    email = db.Column(db.String(255), nullable=False)

    # 定义验证码列，类型为最大长度为255的字符串，不可为空  
    captcha = db.Column(db.String(255), nullable=False)

# 贴吧（博客）表  
class Tiebas(db.Model):  
    # 定义数据库中的表名  
    __tablename__ = 'tieba'

    # 定义贴吧（博客）ID列，类型为整数，是主键且自动增长  
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    # 定义标题列，类型为最大长度为128的字符串  
    title = db.Column(db.String(128))

    # 定义文本内容列，类型为TEXT  
    text = db.Column(db.TEXT)

    # 定义创建时间列，类型为最大长度为64的字符串  
    create_time = db.Column(db.String(64))

    # 定义用户列，存储创建该贴吧（博客）的用户的ID或用户名，类型为最大长度为256的字符串  
    user = db.Column(db.String(256))

    types = db.Column(db.Integer)

# 评论表  
class Comment(db.Model):  
    # 定义数据库中的表名  
    __tablename__ = 'comment'

    # 定义评论ID列，类型为整数，是主键且自动增长  
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    # 定义评论内容列，类型为最大长度为256的字符串  
    text = db.Column(db.String()) 

    # 定义创建时间列，类型为最大长度为64的字符串  
    create_time = db.Column(db.String(64))

    # 定义关联博客ID列，表示该评论属于哪个博客，类型为整数 
    tieba_id = db.Column(db.Integer)

    # 定义用户列，存储发表该评论的用户的ID或用户名，类型为最大长度为256的字符串  
    user = db.Column(db.String(256))

# 问题表（这里命名可能有些误导，因为字段是answer和question）  
class Questions(db.Model):  
    # 定义数据库中的表名  
    __tablename__ = 'questions'

    # 定义问题ID列，类型为整数，是主键且自动增长  
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  

    # 定义为最大长度为256的字符串  
    answer = db.Column(db.String(256))

    # 定义问题内容列，类型为最大长度为256的字符串  
    question = db.Column(db.String(256))