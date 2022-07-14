# You have 100 computers that centrally log outbound netflow sockets to "netflow.txt".
# You want to alert yourself if any of your devices  start port scanning, as that could indicate compromise.
# The central log file is of this format: "saddr:port -> daddr:port"
#
# Write a script that prints out Source IPs that have connected to >=3 unique ports of each unique Dest IP
#
# For example:
# 192.168.42.1:1337 -> 216.58.195.236:22
# 192.168.42.1:1234 -> 216.58.195.237:22
# 192.168.42.1:5555 -> 216.58.195.238:22
# Should have no output
#
# 192.168.42.1:1234 -> 216.58.195.236:22
# 192.168.42.1:1337 -> 216.58.195.237:23
# 192.168.42.1:5555 -> 216.58.195.238:24
# Should have no output
#
# 192.168.42.2:5555 -> 216.58.195.238:22
# 192.168.42.2:1337 -> 216.58.195.238:80
# 192.168.42.2:1234 -> 216.58.195.238:443
# 192.168.42.1:5555 -> 216.58.195.238:24
# Should output: 192.168.42.2
# https://stackoverflow.com/questions/12330522/how-to-read-a-file-without-newlines

addresses = []

# open file, parse content, build 2d array for storing
my_file = open("netflow.txt", "r")
temp = my_file.read().splitlines()
for x in temp:
    addresses.append(x.split(" -> "))
#    print(x)

# build and populate data structure (2d array) to store the ips and ports
m=[]
count = len(addresses)
for ip in addresses:
    m.append(list((ip[0].split(":"),ip[1].split(":"))))

print(m[0])
print(m[1])
print(m[2])
print(m[0][0][1])


for i in range(count-2):
    if (m[i][0][0] == m[i+1][0][0] == m[i+2][0][0]):
#        print(m[i][0][0],m[i+1][0][0],m[i+2][0][0])
        if (m[i][1][0] == m[i+1][1][0] == m[i+2][1][0]):
#            print(m[i][1][0], m[i+1][1][0], m[i+2][1][0])
            if (m[i][1][1] != m[i+1][1][1] != m[i+2][1][1]):
#                print(m[i][1][1], m[i+1][1][1], m[i+2][1][1])
                print(f' Source IP is {m[i][0][0]}')

if the last 3 source IPs are EQ 
    if the last 3 dst IPs are EQ
        if the last dst ports are NEQ
            return source IP


format looks like...
so m[0] gives ['192.168.42.1', '1337'], ['216.58.195.236', '22']
m[0][0] => ['192.168.42.1', '1337']
m[0][0][0] => 192.168.42.1 #src_ip
m[0][0][1] => 1337 #src_port

"""



