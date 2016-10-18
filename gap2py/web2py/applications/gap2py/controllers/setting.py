# -*- coding: utf-8 -*-
# 尝试
import gluon.contrib.simplejson as sj
from zcommon import *
import os
debug = False
def skin_config():
    user = session.get('user', '')
    if user:
        response.view = 'skin-config.html'
        return dict()
    else:
        return redirect('/gap2py/login/index')

def index():
    if debug:
        print 'index'
    user = session.user
    if user == "midnet":
        return dict(username=user)
    else:
        return redirect('/gap2py/index/index')


def dtype():
    if debug:
        print 'dtype'
    flag = False
    user = session.user
    if user == "midnet":
        try:
            file = "%s%s" % (dpath(), "db/needchange")
            flag = os.path.exists(file);
        except Exception as e:
            print e

        dt = getdtype()
        if flag:
            dt['ct'] = dt['rt']
            dt['cd'] = dt['rd']
            setdtype(dt)
            os.remove(file)

        return sj.dumps(dt)
    else:
        return redirect('/gap2py/login/index')


def sdtype():
    user = session.user or ''
    if user:
        rt = request.vars.rt
        rd = request.vars.rd
        iad = request.vars.iad
        oad = request.vars.oad
        if rt == rd == iad == oad == '-1':
            return sj.dumps({'fb': -1})
        ss = getdtype()
        if int(rt) != -1:
            ss['rt'] = int(rt)
        if int(rd) != -1:
            ss['rd'] = int(rd)
        if int(iad) != -1:
            ss['iad'] = int(iad)
        if int(oad) != -1:
            ss['oad'] = int(oad)
        setdtype(ss)
        if iad == oad == '-1':
            pass
        else:
            setbootcfg(ss)
        return sj.dumps({'fb': 1})
    else:
        return
