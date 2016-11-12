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


def gap_time():
    user = session.get('user', '')
    data = {'succ': False}
    if user:
        import time
        ISOTIMEFORMAT='%Y-%m-%d %X'
        data['time'] = time.strftime( ISOTIMEFORMAT, time.localtime() )
        data['succ'] = True 
    return sj.dumps(data)

def gap_set_time():
    user = session.get('user', '')
    data = {'succ': False}
    if user:
        if request.env.request_method == 'POST':
            time = request.post_vars.time
            os.system("date %s" % time)
    return sj.dumps(data)
# def bytesToSize1024(bytes, precision = 2):
#     import math
#     unit = ('B','KB','MB')
#     if bytes >=1024:
#         i = math.floor(math.log(bytes, 1024))
#         return "%s%s" % (round(bytes / math.pow(1024, i), precision),unit[int(i)-1])
#     else:
#         return "%sB" % bytes

def CalcMD5(filepath):
    import hashlib
    with open(filepath,'rb') as f:
        md5obj = hashlib.md5()
        md5obj.update(f.read())
        hash = md5obj.hexdigest()
        print(hash)
        return hash
def gap_newsystem():
    

    
    file_ = open('newsystem.tar.gz', 'w')
    for x in request.post_vars['image_file'].file.readlines():
        file_.write(x)
    file_.close()
    
    return '''<p>上传完毕！MD5验证码：%s</p>''' % CalcMD5('newsystem.tar.gz')
    
