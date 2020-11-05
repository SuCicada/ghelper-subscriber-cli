# def host2ip(host):
import socket
from urllib.parse import urlparse, urlunparse

"""
    for pass that forbid env-proxy host by aliyun
    translate the host to ip in env.profile
"""
if __name__ == '__main__':
    env_profile = "env.profile"
    proxy = []
    with open(env_profile, 'r') as env:
        proxy = env.readlines()
        # cfg.write(cfg_file)
    proxy = map(lambda s: s.split("="), proxy)

    res = []
    for prefix, p in proxy:
        arr = urlparse(p)
        host = str(arr.hostname)
        print(host)
        ip = socket.gethostbyname(host)
        print(ip)
        netloc = "{}:{}@{}:{}".format(arr.username, arr.password, ip, arr.port)
        print(netloc)
        good_url = arr._replace(netloc=netloc).geturl()
        print(good_url)
        res += (prefix + "=" + good_url)

    with open(env_profile, 'w') as env:
        env.writelines(res)
