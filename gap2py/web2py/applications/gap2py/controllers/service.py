import gluon.contrib.simplejson as sj
from zcommon import *
import os

def need_restart():
    data = {'succ': False}
    user = session.get('user', '')
    if user:
        try:
            file = "%s%s" % (dpath(), "db/needrestart")
            data['succ'] = os.path.exists(file);
        except Exception as e:
            print e
            data['succ'] = False
    else:
        return redirect('/gap2py/login/index')
    return sj.dumps(data)

def online():
    return sj.dumps({'fb': '1'})

def gap_reload():
    user = session.get('user', '')
    if user:
        if request.env.request_method == 'POST':
            cmd = request.post_vars.cmd
            password = request.post_vars.password
            if cmd == 'reload':
                if password == 'zll':
                    restart_gap()
    return sj.dumps({})

def gap_stop():
    user = session.get('user', '')
    if user:
        if request.env.request_method == 'POST':
            cmd = request.post_vars.cmd
            password = request.post_vars.password
            if cmd == 'stop':
                if password == 'zll':
                    stop_gap()
    return sj.dumps({})



def doitquick():
    user = session.get('user', '')
    if user:
        if request.env.request_method == 'POST':
            cmd = request.post_vars.cmd
            password = request.post_vars.password
            mash = request.post_vars.mash
            if cmd == 'arp':
                if mash == 'ia':
                    pass
                elif mash == 'oa':
                    pass
                else:
                    pass
    return sj.dumps({})








def gap_newsystem():
    user = session.get('user', '')
    data = {'succ': False}
    if user:

    
        file_ = open('newsystem.tar.gz', 'w')
        for x in request.post_vars['image_file'].file.readlines():
            file_.write(x)
        file_.close()
        
        return '''<p>上传完毕！MD5验证码：%s,</p>''' % CalcMD5('newsystem.tar.gz')
    return sj.dumps(data)
