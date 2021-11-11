import random
import re
import string


def validatePhoneNumberFormat(address):
    phoneNumberPattern = re.compile("^(\\+|[1-9])[0-9]{0,14}$", re.IGNORECASE)
    whatsappPattern = re.compile("^whatsapp:(\\+|[1-9])[0-9]{0,14}$", re.IGNORECASE)
    messengerPattern = re.compile("^messenger:(\\+|[1-9])[0-9]{0,14}$", re.IGNORECASE)
    weChatPattern = re.compile("^wechat:[a-zA-Z0-9+\\-_@.]{1,248}$", re.IGNORECASE)

    if phoneNumberPattern.match(address):
        return "SMS"
    elif whatsappPattern.match(address):
        return "WHATSAPP"
    elif messengerPattern.match(address):
        return "MESSENGER"
    elif weChatPattern.match(address):
        return "WECHAT"
    else:
        return "INVALID_ADDRESS"


if __name__ == '__main__':
    print(validatePhoneNumberFormat("+15555555555555"))
    print(validatePhoneNumberFormat("+14155552671"))
    print(validatePhoneNumberFormat("WHATSAPP:+155555555OP55555"))
    letters = string.ascii_letters
    x = ''.join(random.choice(letters) for i in range(248))
    print(validatePhoneNumberFormat(f"wechat:{x}"))
    print(validatePhoneNumberFormat(f"wechat:--2++"))
    print(validatePhoneNumberFormat("messenger:+155 5555555"))
    print(validatePhoneNumberFormat("messenger:+14155552671432304321"))
