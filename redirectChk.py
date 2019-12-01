#!/usr/bin/env python3

import requests, argparse

# argparse
parser = argparse.ArgumentParser(description='This is redirect URL checker.')
parser.add_argument('URI', help='target URI')
parser.add_argument('-v', action='store_true', help='vervose full redirect history')
args = parser.parse_args()

# access
resp=requests.get(args.URI)

# show result

if args.v:
  ret = "count|code|url\n"
  ret = ret + "-----+----+-------------------------------\n"

  for x in range(len(resp.history)):
    tmp="{0:5}|{1:4}|{2}\n".format(str(x),str(resp.history[x].status_code),str(resp.history[x].url))
    ret=ret+tmp

  tmp="{0:5}|{1:4}|{2}\n".format(str(len(resp.history)+1),str(resp.status_code),str(resp.url))
  ret = ret+tmp
  print(ret,end="")
else:
  print("{0:4}|{1}\n".format(str(resp.status_code),str(resp.url)),end="")
  #print(tmp)
