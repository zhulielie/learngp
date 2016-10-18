# -*- coding: utf-8 -*-
from mnLicense import MNLicense
from zcommon import *
# 尝试


def getlicense():
    s = {}
    try:
        f = open("%s%s" % (dpath(), "db/license.json"), "r");
        s = json.load(f)

    except Exception as e:
        print e
    finally:
        f.close()
    if s.get('license'):
        return s['license']
    else:
        return ''



def save_license(license):
    s = False
    try:
        f = open("%s%s" % (dpath(), "db/license.json"), "w");
        json.dump({"license": license}, f)
        s = True
    except:
        pass
    finally:
        f.close()
    return s

def index():


    key = ["9878*(&^^&)0LLIu(*&^))#$@!KJLKJj", "8midnet8", b'1815122959500519']
    obj = MNLicense(key)
    status = ''
    cl = ''
    mash = obj.creatmash(obj.creatdict())

    if request.env.request_method == 'GET':
        ol = getlicense()
        cl = ol
        f = False
    else:
        ol = request.post_vars.license or ''
        f = True
    if ol:
        try:

            if obj.checklicense(ol):
                status = 'License ok'
            else:
                status = 'license Error'
            if f:
                save_license(ol)
        except Exception as e:
            print e

    return dict(status=status, mash=mash,cl=cl)
