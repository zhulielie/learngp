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
