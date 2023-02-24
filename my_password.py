#!/bin/python

website = ["UTokyo", "JREC-IN", "Microsoft", "Amazon", "Lastpass", 
			"Rakuten", "d-account", "facebook", "wechat", 
			"apple", "taobao", "line-works"]

info = [{"user_name":"6919211590", "password": "Utoto15....@"}, 
{"user_name":"fuxi1010@gmail.com", "password": "Jobjob333666"},
{"user_name":"kofreesia@outlook.com", "password":"Fukufuyu15.. @"},
{"user_name":"toluckyfamily@gmail.com", "password":"Amaama15...."},
{"user_name":"fuxi1010@gmail.com", "password": "Lastlastx..1..~!@"},
{"user_name":"toluckyfamily@gmail.com", "password": "Rakuraku333666~!@#"},
{"user_name":"fuxi1010", "password": "Dd15…."},
{"user_name":"fuxi1010@gmail.com", "password":"Hiface15...."},
{"user_name":"kofreesia", "password": "Chatxx33..~~"},
{"user_name":"kofressia@icloud.com", "password": "A...33..##"},
{"user_name":"riraku_xi", "password": "Zhixx33..##"},
{"user_name":"fu_xi@suikou", "password": "as7&uwEU@RD4"}
]


my_password = dict(zip(website, info))

print(my_password['UTokyo'])

