# -*- coding: utf-8 -*-
# 尝试
def index():
    user = session.get('user', '')
    if user:
        response.view = 'skin-config.html'
        return dict()
    else:
        return redirect('/gap2py/login/index')
