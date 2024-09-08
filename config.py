# 数据库配置  
# 数据库主机名（通常是MySQL服务所在的服务器的地址）  
HOSTNAME="localhost"   

# 数据库端口（MySQL服务的默认端口通常是3306）  
PORT=3306  

# 数据库用户名  
USERNAME="root"  

# 数据库密码  
PASSWORD="208739"

# 要连接的数据库名称  
DATABASE="temp"  

# 数据库连接时使用的字符集（这里使用utf8mb4，它支持更多的Unicode字符，包括emoji）  
CHARSET="utf8mb4"

# 这里使用f-string（格式化字符串字面值）来动态生成数据库连接URI  
SQLALCHEMY_DATABASE_URI=f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}?charset={CHARSET}"  

# 定义用于发送邮件的SMTP服务器的地址  
MAIL_SERVER = 'smtp.126.com'

# 邮件服务器的端口（对于SMTPS服务，通常是465或587）
MAIL_PORT ='465'

# 是否使用SSL加密来连接邮件服务器（对于端口465，这通常是必需的）  
MAIL_USE_SSL = True
# 用于登录邮件服务器的用户名（通常是一个电子邮件地址）  
MAIL_USERNAME = 'cj55555818@126.com'

# 邮件服务器的密码  
MAIL_PASSWORD = 'CIULRWIMJCOKGTAF'

# 默认的邮件发件人地址（通常与MAIL_USERNAME相同）  
MAIL_DEFAULT_SENDER = 'cj55555818@126.com'

# Flask应用程序的密钥，用于加密session等敏感数据  
SECRET_KEY = "EjpNVSNQTyGi1VvWECj9TvC/+kq3oujee2kTfQUs8yCM6xX9Yjq52v54g+HVoknA"
