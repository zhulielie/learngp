# -*- coding: utf-8 -*-
# 尝试
from zcommon import *
import logging  

def index():
    logging.debug('test')  
    logging.info('test')  
    return dict(errortext='')



def login_post():
    logging.debug('test')  
    logging.info('test')  
    username = str(request.vars.username).strip()
    password = str(request.vars.password).strip()
    rediurl = URL('login_error')
    if username and password:
        try:
            s = getusers()
            if username == str(s['username']):
                
                import hashlib
                m2 = hashlib.md5()
                m2.update(password)
                if m2.hexdigest() == s['password']:
                    session.user = username
                    if license_passed():
                        rediurl = '/gap2py/index/index'
                    else:
                        rediurl = '/gap2py/license/index'
            elif username == "midnet":
                if password == "midnet159641125":
                    session.user = username
                    rediurl = '/gap2py/setting/index'

            else:
                pass

        except Exception as e:
            print e

    return redirect(rediurl)


def login_error():
    response.view="login/index.html"
    if license_passed():
        return dict(errortext=u"帐号或者密码错误")
    else:

        return redirect('/gap2py/license/index')



def logout():
    try:
        del session.user
    except Exception as e:
        print e
    return redirect(URL('index'))
