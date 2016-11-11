import json
import binascii
import os
import base64
from Crypto.Cipher import AES
from pyDes import *


class MNCrypt():
    def __init__(self, key):
        self.key = key
        self.mode = AES.MODE_CBC

    def mnencrypt(self, text):
        cryptor = AES.new(self.key[0], self.mode, self.key[2])
        length = 16
        count = text.count('')
        if count < length:
            add = (length - count) + 1
            text = text + (' ' * add)
        elif count > length:
            add = (length - (count % length)) + 1
            text = text + (' ' * add)
        return cryptor.encrypt(text)

    def mndecrypt(self, text):
        cryptor = AES.new(self.key[0], self.mode, self.key[2])
        return cryptor.decrypt(text)


class MNLicense():
    def __init__(self, key, ):
        self.key = key

    def creatmash(self, dict={}):
        en = MNCrypt(self.key)
        if dict:
            data = binascii.b2a_base64(en.mnencrypt(json.dumps(dict)))
        else:
            data = binascii.b2a_base64(en.mnencrypt(json.dumps(self.creatdict())))
        kd = des(self.key[1], CBC, "\0\0\0\0\0\0\0\0", pad=None, padmode=PAD_PKCS5)
        return base64.encodestring(kd.encrypt(data))

    def dumpmash(self):
        print self.creatmash(self.creatdict())

    def dumpdict(self):
        print self.creatdict()

    def creatdictWithlicense(self, oldlicense):
        kd = des(self.key[1], CBC, "\0\0\0\0\0\0\0\0", pad=None, padmode=PAD_PKCS5)
        en = MNCrypt(self.key)
        return json.loads(
            en.mndecrypt(binascii.a2b_base64(kd.decrypt(base64.decodestring(self.license2mash(oldlicense))))))

    def creatdictWithmash(self, mash):
        kd = des(self.key[1], CBC, "\0\0\0\0\0\0\0\0", pad=None, padmode=PAD_PKCS5)
        en = MNCrypt(self.key)
        return json.loads(en.mndecrypt(binascii.a2b_base64(kd.decrypt(base64.decodestring(mash)))))

    def dumpdictWithlicense(self, oldlicense):
        print self.creatdictWithlicense(self, oldlicense)

    def creatdict(self, longlic=1, start_date='', end_date='', dev_no=-1, ints_num=0):
        dict = {}
        dict['longlic'] = longlic
        dict['start_date'] = start_date
        dict['end_date'] = end_date
        dict['dev_no'] = dev_no
        dict['ints_num'] = ints_num
        ifconfig = '/sbin/ifconfig'
        grep = '/usr/bin/grep'
        awk = '/usr/bin/awk'
        sysctl = '/sbin/sysctl'
        smartctl = '/usr/local/sbin/smartctl'
        get_card = "%s -a /dev/%s | %s 'Serial Number' | %s '{print $3}'"
        ads = ['ada0']
        if dict['dev_no'] == -1:
            for x in range(len(ads)):
                card_searial = os.popen(get_card % (smartctl, ads[x], grep, awk)).read().strip('\n')
                if card_searial != "":
                    dict['dev_no'] = x
                    break
        else:
            card_searial = os.popen(get_card % (smartctl, ads[dict['dev_no']], grep, awk)).read().strip('\n')
        info_cpu = os.popen("%s hw.model | %s '{$1=\"\";print $0}' " % (sysctl, awk)).read().strip('\n')
        info_mem = os.popen("%s hw.realmem | %s '{$1=\"\";print $0}' " % (sysctl, awk)).read().strip('\n')
        info_macs = []
        dict['CPU'] = info_cpu.strip()
        dict['MEM'] = info_mem.strip()
        dict['DISK'] = card_searial.strip()
        # dict['OPT1'] = ""
        # dict['TYPE'] = "GAP"
        interfaces = ["%s%s" % (y,x) for y in ['igb'] for x in range(0,8)]
        for x in range(len(interfaces)):
            mac = os.popen(
                "%s %s lladdr | %s ether | %s '{print $2}'l" % (ifconfig, interfaces[x], grep, awk)).read().strip('\n')
            if mac:
                info_macs.append('%s:%s' % (interfaces[x], mac))
                dict['ints_num'] = dict['ints_num'] + 1
        dict['NC'] = info_macs
        return dict

    def creatlicense(self):
        return self.mash2license(self.creatmash(self.creatdict()))

    def dumplicense(self):
        print self.creatlicense()

    def mash2license(self, mash):
        if not mash.endswith('\n'):
            mashstr = mash + '\n'
        else:
            mashstr = mash
        en = MNCrypt(self.key)
        return binascii.b2a_base64(en.mnencrypt(mashstr))

    def license2mash(self, lic):
        en = MNCrypt(self.key)
        return en.mndecrypt(binascii.a2b_base64(lic))

    def checklicense(self, oldlicense):
        try:
            realdict = self.creatdict()
            calcdict = self.creatdictWithlicense(oldlicense)
            realdictkeys = realdict.keys()
            for k in realdictkeys:
                if realdict[k] != calcdict[k]:
                    return False

        except Exception as e:
            print str(e)
            return False
        return True


    def checkmash(self, mash):
        return self.creatdict() == self.creatdictWithmash(mash)
