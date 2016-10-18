import platform,json
import time,os
import threading,thread


def getplatform():
    return platform.system() == 'Darwin'
def dpath():

    tp = "/usr/nc-home/gap2py/web2py/applications/gap2py/static/"
    if getplatform():
        tp = "/Users/zhulielie/PycharmProjects/gap2py/web2py/applications/gap2py/static/"
    return tp


def rsetting():
    s = {}
    s['host'] = '2.2.2.2'
    s['port'] = 51222
    s['username'] = 'gap'
    s['password'] = 'midnetgap'
    s['root_pwd'] = 'midnet66'

    return s


def setusers(users):
    try:
        f = open("%s%s" % (dpath(), "db/user.json"), "w");
        s = json.dump(users, f)
        flag = True
    except:
        flag = False
    finally:
        f.close()

    return flag

def getdtype():
    s = {}
    try:
        f = open("%s%s" % (dpath(), "db/d.json"), "r");
        s = json.load(f)
    except Exception as e:
        print e

    finally:
        f.close()

    return s


def setbootcfg(d):
    os.system('boot0cfg -B -v -o noupdate -t 185 ad%s' % d['iad'])
    verification_ssh(rsetting(), 'boot0cfg -B -v -o noupdate -t 185 ad%s' % d['oad'])

def setdtype(d):
    try:
        f = open("%s%s" % (dpath(), "db/d.json"), "w");
        s = json.dump(d, f)
        flag = True
    except:
        flag = False
    finally:
        f.close()

    return flag

def getusers():
    s = {}
    try:
        f = open("%s%s" % (dpath(), "db/user.json"), "r");
        s = json.load(f)
    except Exception as e:
        print e

    finally:
        f.close()

    return s


import paramiko, time


def verification_ssh(d,cmd):

    host = d['host']
    username = d['username']
    password = d['password']
    port = d['port']
    root_pwd = d['root_pwd']

    s = paramiko.SSHClient()
    s.load_system_host_keys()
    s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    s.connect(hostname=host, port=int(port), username=username, password=password)
    if username != 'root':
        ssh = s.invoke_shell()
        time.sleep(0.1)
        ssh.send('su - \n')
        buff = ''
        while not buff.endswith('Password:'):
            resp = ssh.recv(9999)
            buff += resp
        ssh.send(root_pwd)
        ssh.send('\n')
        buff = ''
        while not buff.endswith('# '):
            resp = ssh.recv(9999)
            buff += resp
        ssh.send(cmd)
        ssh.send('\n')
        buff = ''
        while not buff.endswith('# '):
            resp = ssh.recv(9999)
            buff += resp
        s.close()
        result = buff
    else:
        stdin, stdout, stderr = s.exec_command(cmd)
        result = stdout.read()
        s.close()
    return result
def license_passed():
    return False

def setconfig(config):
    try:
        f = open("%s%s" % (dpath(), "db/config.json"), "w");
        json.dump(config, f)
        try:
            dt = getdtype()
            config['dt'] = dt
            threads = []
            threads.append(threading.Thread(target=write_ia_rcconf,args=(config['ia'],)))

            threads.append(threading.Thread(target=write_oa_rcconf,args=(config['oa'],)))

            threads.append(threading.Thread(target=write_ia_rclocal,args=(config,)))

            threads.append(threading.Thread(target=write_oa_rclocal,args=(config,)))

            threads.append(threading.Thread(target=write_ia_router,args=(config['ia']['router'],)))

            threads.append(threading.Thread(target=write_oa_router,args=(config['oa']['router'],)))

            threads.append(threading.Thread(target=write_ia_carp,args=(config['ia']['hs'],)))

            threads.append(threading.Thread(target=write_oa_carp,args=(config['oa']['hs'],)))

            threads.append(threading.Thread(target=write_ia_sox,args=(config,)))

            threads.append(threading.Thread(target=write_oa_sox,args=(config,)))


            if dt['rt'] == 1:

                threads.append(threading.Thread(target=write_ia_detail,args=(config,)))

                threads.append(threading.Thread(target=write_oa_detail,args=(config,)))


            for t in threads:
                t.start()



            verification_ssh(rsetting(),'/usr/nc-home/bin/UpdateDisk')
            try:
                n = open("%s%s" % (dpath(), "db/needrestart"), 'w')
            except Exception as e:
                print e
            finally:
                n.close()
        except Exception as e:
            print e

        flag = True
    except Exception as e:
        print e
        flag = False
    finally:
        f.close()

    return flag

# def setconfig(config):
#     try:
#         f = open("%s%s" % (dpath(), "db/config.json"), "w");
#         json.dump(config, f)
#         try:
#             dt = getdtype()
#             config['dt'] = dt
#
#             write_ia_rcconf(config['ia'])
#             print 'write_ia_rcconf over'
#             write_oa_rcconf(config['oa'])
#             print 'write_oa_rcconf over'
#             write_ia_rclocal(config)
#
#             print  'write_ia_rclocal over'
#             write_oa_rclocal(config)
#             print  'write_oa_rclocal over'
#             write_ia_router(config['ia']['router'])
#             print  'write_ia_router over'
#             write_oa_router(config['oa']['router'])
#             print  'write_oa_router over'
#             write_ia_carp(config['ia']['hs'])
#             print  'write_ia_carp over'
#             write_oa_carp(config['oa']['hs'])
#             print  'write_oa_carp over'
#             write_ia_sox(config)
#             print  'write_ia_sox over'
#             write_oa_sox(config)
#             print  'write_oa_sox over'
#             if dt['rt'] == 1:
#                 write_ia_detail(config)
#                 print  'write_ia_detail over'
#                 write_oa_detail(config)
#                 print  'write_oa_detail over'
#
#             verification_ssh(rsetting(),'/usr/nc-home/bin/UpdateDisk')
#             try:
#                 n = open("%s%s" % (dpath(), "db/needrestart"), 'w')
#             except Exception as e:
#                 print e
#             finally:
#                 n.close()
#         except Exception as e:
#             print e
#
#         flag = True
#     except Exception as e:
#         print e
#         flag = False
#     finally:
#         f.close()
#
#     return flag

def write_oa_detail(config):
    if config['dt']['rd'] == 2:
        rs = ["IN_TCP", "IN_UDP", "IN_FTP", "IN_ORA"]
    elif config['dt']['rd'] == 1:
        rs = ["OUT_TCP", "OUT_UDP", "OUT_FTP", "OUT_ORA"]
    else:
        rs = ["OUT_TCP", "OUT_UDP", "OUT_FTP", "OUT_ORA", "IN_TCP", "IN_UDP", "IN_FTP", "IN_ORA"]
    for i in rs:
        if config[i]['on'] == '1':
            write_oarule(i, config[i]['rules'])



def write_oa_rcconf(config):
    if getplatform():
        tmp_rc = open("%s%s" % (dpath(), "db/oa/rc.conf"), "w")
    else:
        tmp_rc = '/etc/rc.conf'

    oacontent = '''echo 'sshd_enable="YES"' > %s;''' % tmp_rc
    oacontent += '''echo 'update_motd="NO"' >> %s;''' % tmp_rc
    oacontent += '''echo 'gateway_enable="YES"' >> %s;''' % tmp_rc
    oacontent += '''echo 'syslogd_enable="YES"' >> %s;''' % tmp_rc
    oacontent += '''echo 'syslogd_flags="-ss" ' >> %s;''' % tmp_rc
    if config['defaultgateway']:
        oacontent += '''echo 'defaultrouter="%s"' >> %s;''' % (config['defaultgateway'], tmp_rc)
    oacontent += '''echo 'hostname="MFOA"' >> %s;''' % tmp_rc
    for i in config['interface']:
        oacontent += '''echo 'ifconfig_%s="inet %s netmask %s"' >> %s;''' % (
            i['name'], i['adr'], i['netmask'], tmp_rc)
    oacontent += '''echo 'ifconfig_em4="inet 2.2.2.2 netmask 255.255.255.0"' >> %s;''' % tmp_rc
    oacontent += '''echo 'ifconfig_em5="inet 5.5.5.2 netmask 255.255.255.0"' >> %s;''' % tmp_rc
    if getplatform():
        tmp_rc.write(oacontent)
        tmp_rc.close()
    else:
        try:
            verification_ssh(rsetting(), oacontent)
        except Exception as e:
            print e


def write_oa_rclocal(config):
    if getplatform():
        tmp_rc = open("%s%s" % (dpath(), "db/oa/rc.local"), "w")
    else:
        tmp_rc = '/etc/rc.local'
    adx = str(config['dt']['oad'])

    oacontent = '''echo 'fsck_ufs -y /dev/ad%ss2 >/dev/null' > %s;''' % (adx, tmp_rc)
    oacontent += '''echo 'mount /dev/ad%ss2 /usr/nc-home' >> %s;''' % (adx, tmp_rc)
    oacontent += '''echo 'if [ -f /usr/nc-home/baktgz/patch.tgz ]; then' >> %s;''' % (tmp_rc)
    oacontent += '''echo '	tar xzfP /usr/nc-home/baktgz/patch.tgz' >> %s;''' % (tmp_rc)
    oacontent += '''echo '	rm /usr/nc-home/baktgz/patch.tgz' >> %s;''' % (tmp_rc)
    oacontent += '''echo 'fi' >> %s;''' % (tmp_rc)
    oacontent += '''echo 'ifconfig em5 up' >> %s;''' % (tmp_rc)
    oacontent += '''echo 'sleep 2' >> %s;''' % (tmp_rc)
    oacontent += '''echo 'ifconfig em4 up' >> %s;''' % (tmp_rc)
    oacontent += '''echo 'sleep 2' >> %s;''' % (tmp_rc)
    oacontent += '''echo 'sh /etc/router.conf' >> %s;''' % (tmp_rc)
    oacontent += '''echo 'sh /etc/carp.conf' >> %s;''' % (tmp_rc)
    if config['dt']['rt'] == 1:
        oacontent += '''echo 'sysctl -w hw.owd_recvif=em5' >> %s;''' % (tmp_rc)
        oacontent += '''echo 'sysctl -w hw.owd_sendif=em5' >> %s;''' % (tmp_rc)
        oacontent += '''echo 'cd /usr/nc-home/bin/ && ./prog.sh &' >> %s;''' % (tmp_rc)
        oacontent += '''echo 'cd /usr/nc-home/socks && ./sockd -D -f socks.conf' >> %s;''' % (tmp_rc)
    else:
        oacontent += '''echo 'ipnat -CF -f /usr/nc-home/sox/nsox.cf' >> %s;''' % (tmp_rc)

    if getplatform():
        tmp_rc.write(oacontent)
        tmp_rc.close()
    else:
        try:
            verification_ssh(rsetting(), oacontent)
        except Exception as e:
            print e


def write_oa_router(config):
    if getplatform():
        tmp_rc = open("%s%s" % (dpath(), "db/oa/router.conf"), "w")
    else:
        tmp_rc = '/etc/router.conf'

    oacontent = ''
    begin = True

    for i in config:
        oacontent += '''echo 'route add %s %s %s' %s /etc/router.conf;\n''' % (
            i['network'], i['gateway'], i['netmask'], '> ' if begin else '>>')
        begin = False
    if not config:
        oacontent = '''echo '' > /etc/router.conf;\n'''
    if getplatform():
        try:
            tmp_rc.write(oacontent)
        except Exception as e:
            print e
        finally:
            tmp_rc.close()
    else:

        try:
            verification_ssh(rsetting(), oacontent)
        except Exception as e:
            print e


def write_oa_carp(config):
    oacontent = ''
    begin = True
    # for i in config['rules']:

    if getplatform():
        tmp_rc = open("%s%s" % (dpath(), "db/oa/carp.conf"), "w")

    if config['on'] == '0' or not config['rules']:
        oacontent = '''echo '' > /etc/carp.conf;'''
    else:
        for i in config['rules']:
            if (i['on'] == '1'):
                oacontent += '''echo 'ifconfig carp%s create %s netmask %s vhid %s advskew %s' %s /etc/carp.conf; ''' % (
                    i['gid'], i['adr'], i['netmask'], i['gid'], '100' if i['master'] == '1' else '101',
                    '> ' if begin else '>>')

                begin = False
    try:
        if getplatform():
            tmp_rc.write(oacontent)
        else:
            verification_ssh(rsetting(), oacontent)
    except Exception as e:
        print "write oa carp error:%s" % str(e)


def write_oa_sox(config):
    if getplatform():
        tmp_sox = open("%s%s" % (dpath(), "db/oa/nsox.conf"), "w")
    else:
        if config['dt']['rt'] == 0:

            tmp_sox = '/usr/nc-home/sox/nsox.conf'
        else:
            tmp_sox = '/usr/nc-home/sox/sox.conf'

    if config['dt']['rt'] == 0:
        flag_type = config['dt']['rd']
        oacontent = ''
        if flag_type == 2:
            # jinzhuru
            if config["IN_TCP"]['on'] == '1':
                oacontent += '''echo 'map em4 0.0.0.0/0 -> 0/32' > %s;''' % tmp_sox
                for rule in config['IN_TCP']['rules']:
                    oacontent += '''echo 'rdr em0 %s/32 port %s -> 2.2.2.2 port %s' >>%s;''' % (
                        rule['myadr'], rule['myport'], rule['myport'], tmp_sox)



        elif flag_type == 1:
            # jinzhunchu

            if config["OUT_TCP"]['on'] == '1':
                oacontent += '''echo 'map em0 0.0.0.0/0 -> 0/32' > %s;''' % tmp_sox
                for rule in config['OUT_TCP']['rules']:
                    oacontent += '''echo 'rdr em4 0.0.0.0/0 port %s -> %s port %s' >>%s;''' % (
                        rule['myport'], rule['hisadr'], rule['hisport'], tmp_sox)
        else:
            # zhunru he zhunchu
            if config["IN_TCP"]['on'] == '1':

                oacontent += '''echo 'map em4 0.0.0.0/0 -> 0/32' > %s;''' % tmp_sox
                for rule in config['IN_TCP']['rules']:
                    oacontent += '''echo 'rdr em0 %s/32 port %s -> 2.2.2.2 port %s' >>%s;''' % (
                        rule['myadr'], rule['myport'], rule['myport'], tmp_sox)

            if config["OUT_TCP"]['on'] == '1':
                oacontent += '''echo 'map em0 0.0.0.0/0 -> 0/32' %s %s;''' % (
                ">>" if config["IN_TCP"]['on'] == '1' else ">", tmp_sox)
                for rule in config['OUT_TCP']['rules']:
                    oacontent += '''echo 'rdr em4 0.0.0.0/0 port %s -> %s port %s' >>%s;''' % (
                        rule['myport'], rule['hisadr'], rule['hisport'], tmp_sox)
    else:
        oacontent = '''echo 'COMMIN=/dev/owd0' > %s;''' % tmp_sox
        oacontent += '''echo 'COMMOUT=/dev/owd0' >> %s;''' % tmp_sox

        flag_type = config['dt']['rd']
        if flag_type == 2:
            # jinzhuru

            rs = ["IN_TCP", "IN_UDP", "IN_FTP", "IN_ORA"]

        elif flag_type == 1:
            # jinzhunchu
            rs = ["OUT_TCP", "OUT_UDP", "OUT_FTP", "OUT_ORA"]

        else:

            rs = ["OUT_TCP", "OUT_UDP", "OUT_FTP", "OUT_ORA", "IN_TCP", "IN_UDP", "IN_FTP", "IN_ORA"]
        for i in rs:
            if config[i]['on'] == '1':
                oacontent += '''echo 'FILE=/usr/nc-home/sox/%s'>> %s;''' % (i, tmp_sox)
        oacontent += '''echo 'LOG=1' >> %s;''' % tmp_sox
        oacontent += '''echo 'TCPIDLETIMEOUT=604800' >> %s;''' % tmp_sox
        realpath = '/usr/nc-home/sox/sox.conf.new'

    if getplatform():
        tmp_sox.write(oacontent)
        tmp_sox.close()
    else:
        try:
            print oacontent
            verification_ssh(rsetting(), oacontent)
        except Exception as e:
            print e


def write_ia_rcconf(config):
    try:
        if getplatform():
            bsdfile_rcconf = open("%s%s" % (dpath(), "db/ia/rc.conf"), "w")
        else:
            bsdfile_rcconf = open("/etc/rc.conf", "w")
        iacontent = 'sshd_enable="YES"\n'
        iacontent += 'update_motd="NO"\n'
        iacontent += 'gateway_enable="YES"\n'
        iacontent += 'fsck_enable="YES"\n'  # add
        iacontent += 'syslogd_enable="YES"\n'
        iacontent += 'syslogd_flags="-ss"\n'
        if config['defaultgateway']:
            iacontent += 'defaultrouter="%s"\n' % config['defaultgateway']
        iacontent += 'hostname="MFIA"\n'
        # ind = 0
        # tmp = ''
        for i in config['interface']:

            # if tmp == i['name']:
            #     ind += 1
            # else:
            #     pass
            # tmp = i['name']
            iacontent += 'ifconfig_%s="inet %s netmask %s"\n' % (i['name'], i['adr'], i['netmask'])
            # iacontent += 'ifconfig_%s_alias%s="inet %s netmask %s"\n' % (i['name'], ind, i['adr'], i['netmask'])


        iacontent += 'ifconfig_em4="inet 2.2.2.1 netmask 255.255.255.0"\n'
        iacontent += 'ifconfig_em5="inet 5.5.5.1 netmask 255.255.255.0"\n'
        bsdfile_rcconf.write(iacontent)
        bsdfile_rcconf.close()
        flag = True
    except Exception as e:
        print e
        flag = False
    finally:
        if bsdfile_rcconf:
            bsdfile_rcconf.close()
    return flag


def write_ia_rclocal(config):
    try:
        if getplatform():
            bsdfile_rcconf = open("%s%s" % (dpath(), "db/ia/rc.local"), "w")
        else:
            bsdfile_rcconf = open("/etc/rc.local", "w")

        iacontent = 'if [ -f /usr/nc-home/baktgz/patch.tgz ]; then\n'
        iacontent += '	tar xzfP /usr/nc-home/baktgz/patch.tgz\n'
        iacontent += '	rm /usr/nc-home/baktgz/patch.tgz\n'
        iacontent += 'fi\n'
        iacontent += 'ifconfig em4 up\n'
        iacontent += 'sleep 2\n'
        iacontent += 'ifconfig em5 up\n'
        iacontent += 'sleep 2\n'
        iacontent += 'ln -s /usr/nc-home/local /usr/local\n'
        iacontent += 'ln -s /usr/nc-home/libstdc++.so.6 /usr/lib/libstdc++.so.6\n'
        iacontent += 'ln -s /usr/nc-home/uniq /usr/bin/uniq\n'
        iacontent += 'sh /etc/router.conf\n'
        iacontent += 'sh /etc/carp.conf\n'
        if config['dt']['rt'] == 1:
            iacontent += 'sysctl -w hw.owd_recvif=em5\n'
            iacontent += 'sysctl -w hw.owd_sendif=em5\n'
            iacontent += 'cd /usr/nc-home/bin/ && ./prog.sh &\n'
            iacontent += '/usr/nc-home/bin/db.sh\n'
        else:

            iacontent += 'ipnat -CF -f /usr/nc-home/sox/nsox.cf\n'

        bsdfile_rcconf.write(iacontent)
        bsdfile_rcconf.close()
        flag = True
    except Exception as e:
        print e
        flag = False
    finally:
        if bsdfile_rcconf:
            bsdfile_rcconf.close()
    return flag


def write_ia_router(config):
    try:
        if getplatform():
            bsdfile_router = open("%s%s" % (dpath(), "db/ia/router.conf"), "w")
        else:
            bsdfile_router = open("/etc/router.conf", "w")
        iacontent = ''
        for i in config:
            iacontent += 'route add %s %s %s\n' % (i['network'], i['gateway'], i['netmask'])
        bsdfile_router.write(iacontent)
        flag = True
    except Exception as e:
        print e
        flag = False
    finally:
        bsdfile_router.close()
    return flag


def write_ia_carp(config):
    try:
        if getplatform():
            bsdfile_router = open("%s%s" % (dpath(), "db/ia/carp.conf"), "w")
        else:
            bsdfile_router = open("/etc/carp.conf", "w")
        iacontent = ''
        if config['on'] == '1':
            for i in config['rules']:
                iacontent += 'ifconfig carp%s create %s netmask %s vhid %s advskew %s\n' % (
                    i['gid'], i['adr'], i['netmask'], i['gid'], '100' if i['master'] == '1' else '101',)
            bsdfile_router.write(iacontent)
        flag = True
    except Exception as e:
        flag = False
        print "Write ia carp error :%s" % str(e)
    finally:
        bsdfile_router.close()
    return flag


def write_ia_sox(config):
    try:
        if getplatform():
            bsdfile_router = open("%s%s" % (dpath(), "db/ia/nsox.conf"), "w")
        else:
            print config['dt']['rt']
            if config['dt']['rt'] == 0:

                bsdfile_router = open("/usr/nc-home/sox/nsox.conf", "w")
            else:
                bsdfile_router = open("/usr/nc-home/sox/sox.conf", "w")

        if config['dt']['rt'] == 0:
            iacontent = ''
            flag_type = config['dt']['rd']

            if flag_type == 2:
                # jinzhunru
                if config["IN_TCP"]['on'] == '1':
                    iacontent += 'map em0 0.0.0.0/0 -> 0/32\n'

                    for rule in config['IN_TCP']['rules']:
                        iacontent += '''rdr em4 0.0.0.0/0 port %s -> %s port %s\n''' % (
                            rule['myport'], rule['hisadr'], rule['hisport'])

            elif flag_type == 1:
                # jinzhunchu

                if config["OUT_TCP"]['on'] == '1':
                    iacontent += 'map em4 0.0.0.0/0 -> 0/32\n'

                    for rule in config['OUT_TCP']['rules']:
                        iacontent += '''rdr em0 %s/32 port %s -> 2.2.2.2 port %s\n''' % (
                            rule['myadr'], rule['myport'], rule['myport'])



            else:
                # zhunru he zhunchu
                print "zhuruhezhunchu"
                if config["OUT_TCP"]['on'] == '1':
                    iacontent += 'map em4 0.0.0.0/0 -> 0/32\n'
                    for rule in config['OUT_TCP']['rules']:
                        iacontent += '''rdr em0 %s/32 port %s -> 2.2.2.2 port %s\n''' % (
                            rule['myadr'], rule['myport'], rule['myport'])

                if config["IN_TCP"]['on'] == '1':

                    iacontent += 'map em0 0.0.0.0/0 -> 0/32\n'
                    for rule in config['IN_TCP']['rules']:
                        iacontent += '''rdr em4 0.0.0.0/0 port %s -> %s port %s\n''' % (
                            rule['myport'], rule['hisadr'], rule['hisport'])
        else:
            iacontent = 'COMMIN=/dev/owd0\n'
            iacontent += 'COMMOUT=/dev/owd0\n'

            flag_type = config['dt']['rd']
            if flag_type == 2:
                rs = ["IN_TCP", "IN_UDP", "IN_FTP", "IN_ORA"]
            elif flag_type == 1:
                rs = ["OUT_TCP", "OUT_UDP", "OUT_FTP", "OUT_ORA"]
            else:
                rs = ["OUT_TCP", "OUT_UDP", "OUT_FTP", "OUT_ORA", "IN_TCP", "IN_UDP", "IN_FTP", "IN_ORA"]
            for i in rs:
                if config[i]['on'] == '1':
                    iacontent += 'FILE=/usr/nc-home/sox/%s\n' % i
            iacontent += 'LOG=0\n'
            iacontent += 'TCPIDLETIMEOUT=604800\n'
        print iacontent
        bsdfile_router.write(iacontent)
        flag = True
    except Exception as e:
        print e
        flag = False
    finally:
        bsdfile_router.close()
    return flag


def write_owdiarule(rulename, rules):
    try:
        if getplatform():
            rfname = open("%s%s%s" % (dpath(), "db/", rulename), "w")
        else:
            rfname = open("%s%s" % ("/usr/nc-home/sox/", rulename), "w")
        cotent = ''
        for rule in rules:
            if rulename in ["OUT_TCP", "OUT_UDP", "OUT_FTP", "OUT_ORA"]:
                cotent += '''PORT=%s:%s\n''' % (rule['myadr'], rule['myport'])
            else:
                cotent += '''SERVER=%s:%s-%s:%s\n''' % (rule['hisadr'], rule['hisport'], rule['myadr'], rule['myport'])
        rfname.write(cotent)
    except Exception as e:
        print e
    finally:
        rfname.close()


def write_owdoarule(rulename, rules):
    cotent = ''
    flag = True
    for rule in rules:
        if rulename in ["IN_TCP", "IN_UDP", "IN_FTP", "IN_ORA"]:
            cotent += '''echo 'PORT=%s:%s' %s  /usr/nc-home/sox/%s;''' % (
                rule['myadr'], rule['myport'], '>' if flag else '>>', rulename)
        else:
            cotent += '''echo 'SERVER=%s:%s-%s:%s' %s /usr/nc-home/sox/%s;''' % (
                rule['hisadr'], rule['hisport'], rule['myadr'], rule['myport'], '>' if flag else '>>', rulename)
        flag = False
    if not rules:
        cotent += '''echo '' > /usr/nc-home/sox/%s;''' % rulename
    try:
        verification_ssh(rsetting(), cotent)
    except Exception as e:
        print e


def write_iarule(rulename, rules):
    cotent = ''
    for rule in rules:
        if rulename in ["OUT_TCP", "OUT_UDP", "OUT_FTP", "OUT_ORA"]:
            cotent += '''PORT=%s:%s\n''' % (rule['myadr'], rule['myport'])
        else:
            cotent += '''SERVER=%s:%s-%s:%s\n''' % (rule['hisadr'], rule['hisport'], rule['myadr'], rule['myport'])

    try:

        if getplatform():
            rfname = open("%s%s%s" % (dpath(), "db/ia/", rulename), "w")
        else:
            rfname = open("%s%s" % ("/usr/nc-home/sox/", rulename), "w")

        rfname.write(cotent)
    except Exception as e:
        print e
    finally:
        rfname.close()


def write_ia_detail(config):
    if config['dt']['rd'] == 2:
        rs = ["IN_TCP", "IN_UDP", "IN_FTP", "IN_ORA"]
    elif config['dt']['rd'] == 1:
        rs = ["OUT_TCP", "OUT_UDP", "OUT_FTP", "OUT_ORA"]
    else:
        rs = ["OUT_TCP", "OUT_UDP", "OUT_FTP", "OUT_ORA", "IN_TCP", "IN_UDP", "IN_FTP", "IN_ORA"]
    for i in rs:
        if config[i]['on'] == '1':
            write_iarule(i, config[i]['rules'])


def write_oarule(rulename, rules):
    cotent = ''
    flag = True
    for rule in rules:
        if rulename in ["IN_TCP", "IN_UDP", "IN_FTP", "IN_ORA"]:
            cotent += '''echo 'PORT=%s:%s' %s  /usr/nc-home/sox/%s;''' % (
                rule['myadr'], rule['myport'], '>' if flag else '>>', rulename)
        else:
            cotent += '''echo 'SERVER=%s:%s-%s:%s' %s /usr/nc-home/sox/%s;''' % (
                rule['hisadr'], rule['hisport'], rule['myadr'], rule['myport'], '>' if flag else '>>', rulename)
        flag = False
    if not rules:
        cotent += '''echo '' > /usr/nc-home/sox/%s;''' % rulename

    if getplatform():
        try:
            rfname = open("%s%s%s" % (dpath(), "db/oa/", rulename), "w")
            rfname.write(cotent)
        except Exception as e:
            print e
        finally:
            rfname.close()
    else:
        try:
            verification_ssh(rsetting(), cotent)
        except Exception as e:

            print e
