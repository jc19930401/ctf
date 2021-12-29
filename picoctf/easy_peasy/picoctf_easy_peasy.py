from pwn import *
a = 32
r = remote('mercury.picoctf.net', 20266)

print(r.recvuntil(b'What data would you like to encrypt?').decode())
r.sendline(b'A'*49968)
print(r.recvuntil(b'What data would you like to encrypt?').decode())
r.sendline(b'\x00'*32)
r.recvline().decode()

key = r.recvline().decode()
print('key is:'+str(key))

r.close()

key = '0x'+key

flag =hex(int(key,16)^int('0x5b1e564b6e415c0e394e0401384b08553a4e5c597b6d4a5c5a684d50013d6e4b',16))

flag = bytes.fromhex(flag[2:]).decode('utf-8')
print('flag is: picoCTF{'+flag+'}')

