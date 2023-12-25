class Config:
    BILL_MGR_URL = "https://my.firstvds.ru/billmgr"
    AUTH_URL = 'https://firstvds.ru/my/auth'
    AUTH_DATA = {
        'email': '',  #
        'password': '',  #
        'is_ul': False,
        'ul_name_mounted': '',
        'ul_name': '',
        'realname': '',
        'phone': '',
        'phone_formated': '',
        'phone_confirm': False,
        'phone_confirm_code': '',
        'g-recaptcha-response': '',
        'error': False,
        'error_text': '',
        'form_type': 'auth',
        'annotation_type': 'default',
        'recaptcha': False,
        'totp': False,
        'totpCode': '',
        'auth_key': '',
        'site': '',
        'pass_view': 'password',
        '__device_id': '',  #
        '__device_name': 'Chrome',
        '__device_system': 'Windows',
        'partner': '',
        'sesid': '',  #
    }
    BOT_TOKEN = ''  #
    DISCORD_CHANNEL_ID = 1  #
