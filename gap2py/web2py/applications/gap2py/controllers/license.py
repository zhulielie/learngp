# -*- coding: utf-8 -*-
from mnLicense import MNLicense
from zcommon import *
# 尝试




def index():
    user = session.get('user', '')
    if user:
        status = ''
        cl = ''
        z = '0'
        if request.env.request_method == 'GET':
            ol = getlicense()
            cl = ol
            f = False
        else:
            ol = request.post_vars.license or ''
            f = True
        if ol:
            try:

                if checkthelicense(ol):
                    status = 'License 正确'
                    z = '1'
                else:
                    status = 'license 错误'
                if f:
                    save_license(ol)
            except Exception as e:
                print e

        return dict(status=status, mash=getmash(),cl=cl,z=z)
    else:
        return redirect('/gap2py/login/index')
