# print('Hello World')


import random
import string

DNS = "2001:4860:4860::8888"
user = "test"
public_key = "0000000000"
preshared_key = "1111111"
AllowedIPs = "8.8.8.8/64"


def test():
    print("This's config for client_wireguard")
    print("")
    config = ("[Peer]" + "\n" +
           "#" + user + "\n" +
           "PublicKey = " + str(public_key) + "\n" +
          "Presharedkey = " + str(preshared_key) + "\n" +
          "AllowedIPs = ")
    return config

print(test())