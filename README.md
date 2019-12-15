# reidirectChecker

This is redirect URL checker

## how to install/use

1. `$ git clone https://github.com/hogehuga/redirectChk.git`
2. `$ cd redirectChk`
3. `$ sudo make install` (install to /usr/local/bin/redirectChk)
4. use 'redirectChk' command.
5. uninstall is `$ sudo make clean`

## useage

```
$ ./redirectChk.py -h
usage: redirectChk.py [-h] [-v] URI

This is redirect URL checker.

positional arguments:
  URI         target URI

optional arguments:
  -h, --help  show this help message and exit
  -v          vervose full redirect history
```

## example

short mode

```
$ ./redirectChk.py http://httpbin.org/status/301
200 |http://httpbin.org/get
$
```

verbose mode

```
$ ./redirectChk.py -v  http://httpbin.org/status/301
count|code|url
-----+----+-------------------------------
0    |301 |http://httpbin.org/status/301
1    |302 |http://httpbin.org/redirect/1
2    |200 |http://httpbin.org/get
$
```

- status/301 -> redirect/1 -> get
