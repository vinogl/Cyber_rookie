from OpenSSL.crypto import PKey, TYPE_RSA, sign
from OpenSSL.crypto import verify, X509


# 生成密钥对
pk = PKey()
pk.generate_key(type=TYPE_RSA, bits=1024)

# 待签名内容
message = str(input('输入签名内容: ')).encode('utf-8')

# 数字签名
signature = sign(pkey=pk, data=message, digest='sha1')
print(signature)

# 验证签名
x509 = X509()
x509.set_pubkey(pk)
verify(x509, signature=signature, data=message, digest='sha1')
