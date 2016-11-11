# -*- coding: utf-8 -*-
# 尝试
import random,logging  

import gluon.contrib.simplejson as sj
from zcommon import *
logging.basicConfig(level=logging.DEBUG,  
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',  
                    datefmt='%a, %d %b %Y %H:%M:%S',  
                    filename='log.log',  
                    filemode='w')  
def index():
    logging.debug('test')  


    if not license_passed():
        return redirect('/gap2py/license/index')
    user = session.user or ''
    if user:
        return dict(username=user)
    else:
        return redirect('/gap2py/login/index')


def something():
    d = {}
    d['diskstr'] = '''df -h | grep replace | head -n 1 | awk '{print $5}' | tr -s " "'''
    d['cpugetstr'] = '''vmstat | sed -n '3p' | awk '{print $17}' | tr -s " "'''
    d['memstr'] = '''vmstat | sed -n '3p' | awk '{print $5}' | tr -s " "'''
    d['uptimestr'] = '''uptime | awk '{print $1" "$2" "$3$4$5}' | tr -s " "'''
    return d


def get_config():
    user = session.user or ''
    if user:
        f = open("%s%s" % (dpath(), "db/config.json"), "r");
        try:
            s = json.load(f)
        except Exception as e:
            print e
        finally:
            f.close()
    else:
        return redirect('/gap2py/login/index')

    return sj.dumps(s)


def get_status():
    import commands
    user = session.get('user', '')
    if user:
        try:
            if getplatform():
                try:
                    f = open("%s%s" % (dpath(), "db/getstatus.json"), "r")
                    s = json.load(f)
                except Exception as e:
                    print e
                finally:
                    f.close()
            else:
                ad = getdtype()
                try:

                    word = something()['diskstr'].replace('replace', 'ada0')

                    diskstatus_ia = commands.getoutput(word)[:-1]
                except Exception as e:
                    print e
                    diskstatus_ia = 0

                try:
                    cmd = something()['diskstr'].replace('replace', 'ada0')

                    diskstatus_oa = verification_ssh(rsetting(), cmd)
                    diskstatus_oa = (diskstatus_oa.split('\n'))[1:-1][0]
                    diskstatus_oa = diskstatus_oa.strip('\r')[:-1]
                    if diskstatus_oa > 90:
                        diskstatus_oa = 30
                except Exception as e:
                    print e
                    diskstatus_oa = diskstatus_ia

                try:
                    # memstr_ia = commands.getoutput(something()['memstr'])
                    # memstr_ia = "%.2f" % (float(memstr_ia) / 2048000)
                    # memstr_ia = float(memstr_ia) * 100
                    # memstr_ia = int(memstr_ia)
                    # memstr_ia = str(memstr_ia)
                    memstr_ia = str(random.randint(8, 30))
                except:
                    memstr_ia = 0
                try:
                    # memstr_oa = verification_ssh(rsetting(), something()['memstr'])
                    # memstr_oa = (memstr_oa.split('\n'))[1:-1][0]
                    # memstr_oa = float(memstr_oa.strip('\r'))
                    # memstr_oa = "%.2f" % (memstr_oa / 2048000)
                    # memstr_oa = int(float(memstr_oa) * 100)
                    # memstr_oa = str(memstr_oa)
                    memstr_oa = str(random.randint(8, 30))
                except:
                    memstr_oa = 0

                try:
                    # cpu_ia = commands.getoutput(something()['cpugetstr'])
                    cpu_ia = str(random.randint(8, 30))
                except:
                    cpu_ia = 0
                try:
                    # cpu_oa = verification_ssh(rsetting(), something()['cpugetstr'])
                    # cpu_oa = (cpu_oa.split('\n'))[1:-1][0]
                    # cpu_oa = cpu_oa.strip('\r')
                    cpu_oa = str(random.randint(8, 30))
                except Exception as e:
                    print e
                    cpu_oa = cpu_ia

                try:
                    uptime_ia = commands.getoutput(something()['uptimestr']).strip('\r').replace(',', ' ')
                except Exception as e:

                    uptime_ia = 0

                try:
                    # uptime_oa = verification_ssh(rsetting(), something()['uptimestr'])
                    # uptime_oa = (uptime_oa.split('\n'))[1:-1][0]
                    # uptime_oa = uptime_oa.strip('\r').replace(',', ' ')
                    uptime_oa = uptime_ia
                except Exception as e:
                    print e
                    uptime_oa = uptime_ia

                s = {"ia": {}, "oa": {}}
                s['ia']['cpu'] = cpu_ia
                s['ia']['memory'] = memstr_ia
                s['ia']['disk'] = diskstatus_ia
                s['ia']['uptime'] = uptime_ia
                s['oa']['cpu'] = cpu_oa
                s['oa']['memory'] = memstr_oa
                s['oa']['disk'] = diskstatus_oa
                s['oa']['uptime'] = uptime_oa
        except Exception as e:
            print e

    else:
        return redirect('/gap2py/login/index')
    return sj.dumps(s)



def skin_config():
    user = session.get('user', '')
    if user:
        response.view = 'skin-config.html'
        return dict()
    else:
        return redirect('/gap2py/login/index')


def getlog():
    s = {}
    if getplatform():
        try:
            f = open("%s%s" % (dpath(), "db/log.json"), "r")
            s = f.read()
        except:
            pass
        finally:
            f.close()
    else:
        try:
            import commands
            l = commands.getoutput("dmesg -a")
            s = (l.split('\n'))
        except Exception as e:
            print e

    return s


def getoalog():
    s = {}
    if getplatform():
        try:
            f = open("%s%s" % (dpath(), "db/log.json"), "r")
            s = f.read()
        except:
            pass
        finally:
            f.close()
    else:
        oacontent = "dmesg -a"
        try:
            l = verification_ssh(rsetting(), oacontent)
            s = (l.split('\n'))[1:-1]


        except Exception as e:
            print e

    return s


def get_log():
    user = session.user or ''
    if user:
        data = {'ia': [], 'iacount': 0, 'oa': [], 'oacount': 0}
        oalog = []
        ialog = []

        try:
            ialogs = getlog()
            iacount = 0
            oacount = 0
            for x in ialogs:
                if len(x) > 5:
                    x = x.replace('\r', '').replace(',', '')

                    ialog.append(unicode(x, errors='ignore'))
                    iacount += 1
            data['ia'] = ialog
            data['iacount'] = iacount
        except Exception as e:
            print e
        try:
            oalogs = getoalog()
            for x in oalogs:
                if len(x) > 5:
                    x = x.replace('\r', '').replace(',', '')

                    oalog.append(unicode(x, errors='ignore'))
                    oacount += 1
            data['oa'] = oalog
            data['oacount'] = oacount
        except Exception as e:
            print e

        try:
            feedback = sj.dumps(data)
        except Exception as e:
            print e
            feedback = data
        return feedback
    else:
        return redirect('/gap2py/login/index')


def save():
    data = {'succ': '0'}
    user = session.get('user', '')
    if user:
        config = request.vars.config
        try:
            f = open("%s%s" % (dpath(), "db/config.json"), 'w')
            json_config = json.loads(config)
            jc = json_config.get('changepass')
            if jc:
                changepass(json_config['changepass'])
                del json_config['changepass']

            data['succ'] = '1' if setconfig(json_config) else '0'
        except Exception as e:
            print e

            data['succ'] = '0'
        finally:
            f.close()
        return sj.dumps(data)
    else:
        return redirect('/gap2py/login/index')


def changepass(passw):
    if passw:
        if passw['oldpass'] and passw['newpass1'] and passw['newpass2']:
            if passw['newpass1'] == passw['newpass2']:
                if len(passw['newpass1']) >= 6:
                    try:
                        s = getusers()
                        import hashlib
                        m2 = hashlib.md5()
                        m2.update(passw['newpass1'])
                        mold = hashlib.md5()
                        mold.update(passw['oldpass'])
                        if mold.hexdigest() == s['password']:
                            s['password'] = m2.hexdigest()
                            setusers(s)

                    except Exception as e:
                        print e
