# DNSaurus

## DNS Speed Test Tool
This is a simple DNS speed test tool written by Wu Yixuan. It allows you to test the speed and availability of DNS servers for specified domains.

# Features
Test the speed of DNS servers for a list of domains.
Specify the DNS server IP addresses or a file containing a list of DNS server IPs.
Set a timeout for DNS resolution.
Perform multiple tests and calculate average response times.
Identify unavailable DNS servers.
# Usage
To use this tool, you can run it from the command line with the following options:
python3 main.py <-d [domains]> <-s [dnsip or dnsfilename]> <-t [timeout]> <-n [numberoftries]>
# Example:
python3 main.py -d 5i.gs,baidu.com -s dns.txt -t 1 -n 3
-d [domains]: Specify the domains you want to test, separated by commas.
-s [dnsip or dnsfilename]: Specify the DNS server IP addresses or provide a file containing a list of DNS server IPs.
-t [timeout]: Set the timeout for DNS resolution in seconds.
-n [numberoftries]: Specify the number of test tries.
# Installation
This tool uses the dnspython library for DNS resolution. If you don't have it installed, the tool will attempt to install it using pip3 when you run it.

# Output
The tool will provide information about the DNS servers tested, including their average response times and package loss. It will also display the results in a tabular format.
Result:
|DNS server ip          |Average time           |Package loss           |
|114.215.126.16         |0.016279840469360353   |0.0                    |
|114.114.114.114        |0.017542719841003418   |0.6                    |
|210.2.4.8              |0.02241663932800293    |0.0                    |
|180.184.2.2            |0.02465208371480306    |0.4                    |
|223.5.5.5              |0.026650190353393555   |0.0                    |
|180.184.1.1            |0.026779651641845703   |0.8                    |
|223.6.6.6              |0.027649068832397462   |0.0                    |
|101.226.4.6            |0.029510974884033203   |0.8                    |
|123.125.81.6           |0.030738274256388348   |0.4                    |
|112.124.47.27          |0.03126769065856934    |0.0                    |
|52.80.52.52            |0.03305530548095703    |0.6                    |
|218.30.118.6           |0.03329050540924072    |0.2                    |
|117.50.10.10           |0.03425741195678711    |0.0                    |
|8.8.8.8                |0.03481569290161133    |0.0                    |
|1.2.4.8                |0.04939615726470947    |0.6                    |
|140.207.198.6          |0.054625940322875974   |0.0                    |
|101.102.103.104        |0.05902533531188965    |0.0                    |
|180.76.76.76           |0.0669703483581543     |0.8                    |
|101.101.101.101        |0.1622840166091919     |0.2                    |
|119.29.29.29           |0.18736553192138672    |0.8                    |

# Repository
The code for this DNS speed test tool is available on GitHub at repository-link.

# Author
Author: Wu Yixuan
Date: 2023-9-26
Version: 1.0.0
Feel free to contribute to the repository or report any issues you encounter.