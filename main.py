# Description: This is a simple DNS speed test tool.
# Author: Wu Yixuan
# Date: 2023-9-26
# Version: 1.0.0
# Repository: https://git.5i.gs/Cutieu/DNSaurus
# Website: https://5i.gs

import sys
import os
import time
import os.path

try:
    import dns.resolver
except ImportError:
    print("Installing dnspython...")
    os.system("pip3 install dnspython")
    import dns.resolver


def test_speed(domain, dnsip, timeout):

    resolver = dns.resolver.Resolver()
    resolver.nameservers = [dnsip]
    start = time.time()
    try:
        resolver.lifetime = timeout
        resolver.resolve(domain)
    except:
        return -1
    end = time.time()
    return end - start


def test_speed_average(domains, dnsip, numberoftries, timeout):
    average_time = 0
    package_loss = 0
    for i in range(numberoftries):
        domain = domains.split(",")[i % len(domains.split(","))]
        speed = test_speed(domain, dnsip, timeout)
        if speed != -1:
            average_time += speed
        else:
            package_loss += 1
    if package_loss == numberoftries:
        return -1, 1
    else:
        return (
            average_time / (numberoftries - package_loss),
            package_loss / numberoftries,
        )


if __name__ == "__main__":
    args = sys.argv
    if len(args) == 1 or args[1] == "--help":
        print(
            "Usage: python3 main.py <-d [domainstocheck]> <-s [dnsip or dnsfilename]> <-t [timeout]> <-n [numberoftries]>"
        )
        print(
            "Example: python3 main.py -d 5i.gs,baidu.com -s dns.txt -t 1 -n 3"
        )
        exit(0)

    domain = "5i.gs,baidu.com"
    dnsip = "dns.txt"
    timeout = 1
    numberoftries = 3
    for i in range(1, len(args), 2):
        if args[i] == "-d":
            domain = args[i + 1]
        elif args[i] == "-s":
                dnsip = args[i + 1]
        elif args[i] == "-t":
            timeout = float(args[i + 1])
        elif args[i] == "-n":
            numberoftries = int(args[i + 1])
        else:
            print(
                "Usage: python3 main.py <-d [domaintocheck]> <-s [dnsip or dnsfilename]> <-t [timeout]> <-n [numberoftries]>"
            )
            print(
                "Example: python3 main.py -d 5i.gs,baidu.com -s dns.txt -t 1 -n 3"
            )
            exit(0)
    if os.path.exists(dnsip):
        with open(dnsip) as f:
            dnsip = (
                f.read()
                .replace("\n", ",")
                .replace(" ", ",")
                .replace("\t", ",")
                .replace(",,", ",")
                .strip(",")
            )
    print("Domains to test: " + domain)
    print("DNS server ips to test: " + dnsip)
    print("Timeout: " + str(timeout))
    print("Number of tries: " + str(numberoftries))

    dnsip = dnsip.split(",")
    result = []
    for i in range(len(dnsip)):
        average_time, package_loss = test_speed_average(
            domain, dnsip[i], numberoftries, timeout
        )
        if package_loss == 1:
            print("DNS server " + dnsip[i] + " is not available")
        else:
            print(
                "DNS server "
                + dnsip[i]
                + " average time: "
                + str(average_time)
                + "s"
                + " package loss: "
                + str(package_loss)
            )
            result.append((dnsip[i], average_time, package_loss))
    result.sort(key=lambda x: x[1])
    print("\n" * 5 + "Result:")
    print("|DNS server ip      \t|Average time      \t|Package loss      \t|")
    for i in range(len(result)):
        print(
            "|"
            + result[i][0]
            + " " * (20 - len(result[i][0]))
            + "\t|"
            + str(result[i][1])
            + " " * (20 - len(str(result[i][1])))
            + "\t|"
            + str(result[i][2])
            + " " * (20 - len(str(result[i][2])))
            + "\t|"
        )
