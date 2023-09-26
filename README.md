# DNSaurus

DNS Speed Test Tool
This is a simple DNS speed test tool written by Wu Yixuan. It allows you to test the speed and availability of DNS servers for specified domains.

Features
Test the speed of DNS servers for a list of domains.
Specify the DNS server IP addresses or a file containing a list of DNS server IPs.
Set a timeout for DNS resolution.
Perform multiple tests and calculate average response times.
Identify unavailable DNS servers.
Usage
To use this tool, you can run it from the command line with the following options:
python3 main.py <-d [domains]> <-s [dnsip or dnsfilename]> <-t [timeout]> <-n [numberoftries]>
Example:
python3 main.py -d 5i.gs,baidu.com -s dns.txt -t 1 -n 3
-d [domains]: Specify the domains you want to test, separated by commas.
-s [dnsip or dnsfilename]: Specify the DNS server IP addresses or provide a file containing a list of DNS server IPs.
-t [timeout]: Set the timeout for DNS resolution in seconds.
-n [numberoftries]: Specify the number of test tries.
Installation
This tool uses the dnspython library for DNS resolution. If you don't have it installed, the tool will attempt to install it using pip3 when you run it.

Output
The tool will provide information about the DNS servers tested, including their average response times and package loss. It will also display the results in a tabular format.

Repository
The code for this DNS speed test tool is available on GitHub at repository-link.

Author
Author: Wu Yixuan
Date: 2023-9-26
Version: 1.0.0
Feel free to contribute to the repository or report any issues you encounter.