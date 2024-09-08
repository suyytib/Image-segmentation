# 导入Flask的redirect函数，该函数用于重定向用户到另一个URL  
from flask import redirect, session   

# 导入functools的 wraps 函数，该函数用于保留原始函数的元数据（如函数名、文档字符串等）  
from functools import wraps  

# 导入Flask的g对象，g对象是一个特殊的对象，它会在每个请求中维护一个上下文，可以用于在函数之间传递数据  
from flask import g  

# 导入Flask的url_for函数，该函数用于动态生成 URL，可以根据视图函数的名称和参数生成 URL  
from flask import url_for

from model import User  

# 定义一个名为captcha__is_login的装饰器函数  
# 该装饰器函数用于检查用户是否已经登录，如果已登录则正常执行被装饰的函数，否则重定向到登录页面  
def captcha__is_login(func):  
    # 使用 wraps 函数包装内部函数inner，以确保inner函数的元数据和func保持一致  

    @wraps(func)
    # 定义内部函数inner，它接受任意数量的位置参数和关键字参数  
    
    def inner(*args, **kwargs):   
        # 检查 g.user_id 是否存在，如果存在则认为用户已经登录  
        if g.user_id:
            user = User.query.get(g.user_id)
            if (session.get("status"))==user.status:
            # 如果用户已登录，则正常执行被装饰的函数func，并返回其结果  
                return func(*args, **kwargs)  
            else:
                 return redirect(url_for('login.login'))  
        
        # 如果用户未登录，则重定向到登录页面的URL  
        # 注意这里假设有一个名为'login.login'的视图函数，用于处理登录请求  
        else:  
            return redirect(url_for('login.login'))  
    # 返回内部函数inner，使其可以替换原函数func  
    return inner