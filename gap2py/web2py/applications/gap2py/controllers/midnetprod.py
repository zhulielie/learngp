from zcommon import *
from Crypto.Cipher import AES
def index():
    user = session.get('user', '')
    if user == 'midnet':
        try:
            if request.env.request_method == 'POST':
                st = request.vars.st or ''
                obj = AES.new('8midnet8openssl8', AES.MODE_CBC, b'0000000000000000')
                try:
                    file_object = open("%s%s" % (dpath(),'db/secret'), 'w')
                    try:

                        st = st + ((16-len(st) % 16) * ' ')
                        file_object.write(obj.encrypt(st))
                    finally:
                        file_object.close()
                except Exception as e:
                    print e
                return dict(current=st)
            else:
                flag = False
                try:
                    file_object = open("%s%s" % (dpath(),'db/secret'),'r')
                    try:
                        all_the_text = file_object.read()

                        flag = True
                    finally:
                        file_object.close()
                except Exception as e:
                    print e

                if flag and all_the_text:
                    try:
                        obj = AES.new('8midnet8openssl8', AES.MODE_CBC, b'0000000000000000')
                        current = obj.decrypt(all_the_text)
                    except Exception as e:
                        print e
                        current = ""
                else:
                    current = ""

                return dict(current=current)

        except Exception as e:
            print e
            return dict()
    else:
        return redirect('/gap2py/login/index')
