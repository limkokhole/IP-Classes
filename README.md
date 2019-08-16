# IP-Classes
Enter an IP address and it tells you what class it belongs to. Includes localhost, private (RFC 1918), and Apipa addresses.

Note that IPv4 addresses classes really don't exist anymore, and have been deprecated in 1993. [See here](https://networkengineering.stackexchange.com/questions/19840/does-cidr-really-do-away-with-ip-address-classes) and [here](https://networkengineering.stackexchange.com/questions/25320/which-ip-class-do-isps-use)

### Usage: 

    $ python ip-classes.py --help
    usage: ip-classes.py [-h] [-d] [ip]

    ip classes

    positional arguments:
    ip          Numeric ip

    optional arguments:
    -h, --help  show this help message and exit
    -d          Debug by printing log.

### Examples of usage:

    $ type -a ip-classes #set as alias in ~/.bash_aliases
    ip-classes is aliased to `python /home/foo/bar/ip-classes.py'

    $ ip-classes 255.255.255.255
    255.255.255.255 is not a valid IP

    $ ip-classes 254.254.254.254
    254.254.254.254 is an E class IP (Experimental)

    $ ip-classes 10.0.0.0
    10.0.0.0 is a Private A class IP

    $ ip-classes 0.0.0.0
    0.0.0.0 is not a valid IP

    $ ip-classes 0.0.0.1
    0.0.0.1 is not a valid IP

    $ ip-classes 169.254.0.0
    169.254.0.0 is an APIPA (Automatic Private IP Addressing) IP

    $ echo -e "127.0.0.1\n8.8.8.8" | while read -r i; do ip-classes $i; done
    127.0.0.1 is a Localhost (Loopback) IP
    8.8.8.8 is an A class IP

    $ dig +short google.com | while read -r i; do ip-classes $i; done
    172.217.24.174 is a B class IP

    $ dig +short twitter.com | while read -r i; do ip-classes $i; done
    104.244.42.65 is an A class IP
    104.244.42.193 is an A class IP

    $ ip-classes 1000
    Invalid IP, try again
    Abort.

    $ ip-classes 127.000.000.001 #this consider valid since ping/curl also can works
    127.000.000.001 is a Localhost (Loopback) IP

<code>#but 8 is not a valid octal number, compatible with ping/curl, [See here.](https://stackoverflow.com/a/33027136/1074998)</code>

    $ ip-classes 192.168.001.008
    Invalid IP. Note that prefix 0 or 0x will treat as octal or hex respectively, which should contains valid character 0-7 or 0-f respectively.
    Abort.

    $ ip-classes 0x7f.0.0.1 #support valid hex, compatible with ping/curl
    0x7f.0.0.1 is a Localhost (Loopback) IP

    $ ip-classes 0x7g.0.0.1
    Invalid IP. Note that prefix 0 or 0x will treat as octal or hex respectively, which should contains valid character 0-7 or 0-f respectively.
    Abort.

