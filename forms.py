# 导入WTForms的Form类和必要的字段类（StringField, PasswordField）  
from wtforms import Form, StringField, PasswordField, SubmitField  

from flask_wtf import FlaskForm

# 导入WTForms的验证器类  
from wtforms.validators import Length, Email, EqualTo, InputRequired, regexp  
# 定义参与注册验证的表单类  
class Register_Form(Form):  
    # 用户名字段，使用StringField类型，并指定验证器 
    # 验证器包括：InputRequired（必填），Length（长度限制在4-20个字符），regexp（正则表达式验证，确保用户名以字母开头，后面可以跟字母、数字、下划线和点）  
    username = StringField(validators=[InputRequired(u"用户名不能为空"), Length(min=4, max=20), regexp('^[A-Za-z0-9_.]*$', 0, '用户名是字母、数字、下划线和点组成')])
    
    # 密码字段，使用PasswordField类型，并指定验证器  
    # 验证器包括：InputRequired（必填），Length（长度限制在6-20个字符）  
    passwd = PasswordField(validators=[InputRequired(u"密码不能为空"), Length(min=6, max=20)])
    
    # 电子邮件字段，使用StringField类型，并指定验证器  
    # 验证器包括：InputRequired（必填），Email（必须是有效的电子邮件地址）  
    email = StringField(validators=[InputRequired(u"邮件不能为空"), Email()])
    
    # 再次输入密码字段，使用PasswordField类型，并指定验证器  
    # 验证器包括：InputRequired（必填），EqualTo（必须与'passwd'字段的值相同）
    re_password = PasswordField(validators=[InputRequired(u"确认密码不能为空"), EqualTo("passwd", u"两次密码不一致")])  

# 定义参与登录验证的表单类  
class Login_Form(Form):  
    # 用户名字段，使用StringField类型，并指定验证器  
    # 验证器包括：InputRequired（必填），Length（长度限制在4-20个字符）  
    user_name = StringField(validators=[InputRequired(u"用户名不能为空"), Length(min=4, max=20)])
    
    # 密码字段，使用PasswordField类型，并指定验证器  
    # 验证器包括：InputRequired（必填），Length（长度限制在6-20个字符）  
    user_passwd = PasswordField(validators=[InputRequired(u"密码不能为空"), Length(min=6, max=20)])

class Retrieve_Form(Form):  
    
    passwd = PasswordField(validators=[InputRequired(u"原密码不能为空")])
    
    email = StringField(validators=[InputRequired(u"邮件不能为空"), Email()])
    
    re_password = PasswordField(validators=[InputRequired(u"新密码不能为空"), Length(min=6, max=20)])  

class SearchForm(FlaskForm):
    contens = StringField('关键词', validators=[InputRequired()])
    submit = SubmitField('搜索')