# Sample code for checking SSID and Key Mismatch Issue
from subprocess import Popen, PIPE

def get_wifi_networks():
    try:
        output = Popen(["nmcli", "-t", "dev", "wifi"], stdout=PIPE)
        networks, err = output.communicate()
        networks = networks.decode("utf-8").strip().split("\n")
        return networks
    except Exception as e:
        print(str(e))

def connect_to_wifi(ssid, key):
    try:
        command = "nmcli device wifi connect {0} password {1}".format(ssid, key)
        Popen(command, shell=True, stdout=PIPE, stderr=PIPE)
    except Exception as e:
        print(str(e))

networks = get_wifi_networks()
for network in networks:
    ssid, key = network.split(":")[1], network.split(":")[2]
    print("SSID: {0}, Key: {1}".format(ssid, key))
    connect_to_wifi(ssid, key)

