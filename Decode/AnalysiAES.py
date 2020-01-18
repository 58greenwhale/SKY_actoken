from Crypto.Cipher import AES


class AESDecrypt:
    iv = '0123456789ABCDEF'
    key = 'jo8j9wGw%6HbxfFn'

    def pkcs7unpadding(self, text):
        length = len(text)
        unpadding = ord(text[length - 1])
        return text[0:length - unpadding]

    def decrypt(self, content):
        key = bytes(self.key, encoding='utf-8')
        iv = bytes(self.iv, encoding='utf-8')
        cipher = AES.new(key, AES.MODE_CBC, iv)
        decrypt_bytes = cipher.decrypt(bytes.fromhex(content))
        result = str(decrypt_bytes, encoding='utf-8')
        result = self.pkcs7unpadding(result)
        return result


result = AESDecrypt()
