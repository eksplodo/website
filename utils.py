import string
from random import Random

from django.core.mail import send_mail
from website.settings import EMAIL_FROM

from users.models import EmailVerifyRecord


def send_verify_email(email, send_type='register'):
    email_verify_record = EmailVerifyRecord()
    code = random_code(16)
    email_verify_record.email = email
    email_verify_record.send_type = send_type
    email_verify_record.code = code
    email_verify_record.save()

    email_title = ''
    email_body = ''

    if send_type == 'register':
        email_title = 'eksplodo博客注册邮件'
        email_body = '欢迎注册eksplodo博客，请点击下方链接进行激活：http://127.0.0.1:8000/active/{0}'.format(code)

        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass

    elif send_type == 'forget':
        email_title = 'eksplodo博客密码找回'
        email_body = '这是一封密码找回邮件，如果不是本人操作，请忽略它，如果是本人操作，请点击下面链接重置密码：http://127.0.0.1:8000/forget/{0}'.format(code)

        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass


def random_code(length=8):
    code = ''
    chars = string.ascii_letters + string.digits
    nums = len(chars) - 1
    random = Random()
    for i in range(length):
        code += chars[random.randint(0, nums)]
    return code