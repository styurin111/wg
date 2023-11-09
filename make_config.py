import random
import string
import sys
from wireguard_tools import WireguardKey


my_list = [sys.argv]
length = 44

class tools():
    def private_key():
        private_key = WireguardKey.generate()
        return str(private_key)

    def public_key(private_key):
        public_key = private_key.public_key()
        return str(public_key)

    def preshared_key(length):
        return ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(length))

class config():

    def create_conf(USER, ADDRESS):
        private_key_client = tools.private_key()
        public_key_server = "o1NMtj0rXQKbYBsYVkB2Dv5N0UHgR6ZrF5S+slt+nhw"
        config = ("####config for client####" + "\n" +
                  "\n" +
                  "#" + USER + "\n" +
                  "[Interface]" + "\n" +
                  "PrivateKey = " + private_key_client + "\n" +
                  "Address = " + ADDRESS + "\n" +
                  "DNS = 2001:4860:4860::8888" + "\n" + "\n" +
                  "[Peer]" + "\n" +
                  "PrivateKey = " + str(public_key_server) + "\n" +
                  "Presharedkey = " + str(tools.preshared_key(length)) + "\n" +
                  "AllowedIPs = 2001:4860:4860::8888, 2001:67c:2b20::/48, 2001:67c:28d4::/48" + "\n" +
                  "PersistentKeepalive = 15" + "\n" +
                  "\n" +
                  "####config for server####" + "\n" +
                  "\n" +
                  "#" + USER + "\n" +
                  "PublicKey = " + str(tools.private_key()) + "\n" +
                  "Presharedkey = " + str(tools.preshared_key(length)) + "\n" +
                  "AllowedIPs = " + ADDRESS)

        return config

for i in my_list:
    print(config.create_conf(i[1], i[2]))



