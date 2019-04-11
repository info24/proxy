import socket
import ssl
import logging
logging.basicConfig(level = logging.INFO,format = ' [%(funcName)s] -%(levelname)s- %(lineno)d : %(message)s')
logger = logging.getLogger(__name__)

def foo():
	s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s = ssl.wrap_socket(s)
	s.connect(('www.baidu.com',443))
	try:
		# 使用sendall才能正确发送
		s.sendall(b'GET / HTTP/1.1\r\nHost: www.baidu.com\r\nAccept-Encoding: identity\r\n\r\n')
		 
		buf=s.recv(1024)
		print(buf.decode("utf-8"))
	finally:
		s.close()

foo()
import sys
sys.exit()
import ssl
from io import BytesIO
import gzip

def run():
	sock = ssl.wrap_socket(socket.socket())
	sock.connect(('zh.lianjia.com', 443))
	sock.send('GET /ershoufang/ HTTP/1.1\r\n'.encode())
	sock.send('Host: zh.lianjia.com\r\n'.encode())
	sock.send('Connection: keep-alive\r\n'.encode())
	sock.send('Cache-Control: no-cache\r\n'.encode())
	sock.send('Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8;charset=utf-8\r\n'.encode())
	sock.send('Upgrade-Insecure-Requests: 1\r\n'.encode())
	sock.send('User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36\r\n'.encode())
	# sock.send('Accept-Encoding: gzip, deflate, br\r\n'.encode())
	sock.send('Cookie: lianjia_uuid=ce61c41c-25b0-46d6-a0a0-d57a75ee8706; UM_distinctid=1631f588055f9-0286722badd3ec-b34356b-1fa400-1631f58805657f; _ga=GA1.2.43397143.1525239286; _smt_uid=5ae94e02.558be516; _jzqx=1.1525248800.1525335927.1.jzqsr=zh%2Elianjia%2Ecom|jzqct=/ershoufang/xiangzhouqu/.-; _jzqc=1; _jzqy=1.1525239284.1525594526.2.jzqsr=baidu.jzqsr=baidu|jzqct=%E9%93%BE%E5%AE%B6; _jzqckmp=1; _gid=GA1.2.1028411676.1525594529; Hm_lvt_9152f8221cb6243a53c83b956842be8a=1525594526,1525594536,1525594804,1525595210; select_city=440400; all-lj=c60bf575348a3bc08fb27ee73be8c666; _qzjc=1; lianjia_ssid=99306d63-8ee5-a53c-a740-2d3021f3db2f; CNZZDATA1255604082=964175865-1525237915-https%253A%252F%252Fwww.lianjia.com%252F%7C1525602095; _jzqa=1.3750161754444366000.1525239284.1525594526.1525603274.8; CNZZDATA1254525948=963210960-1525238218-https%253A%252F%252Fwww.lianjia.com%252F%7C1525603556; CNZZDATA1255633284=1054798284-1525238580-https%253A%252F%252Fwww.lianjia.com%252F%7C1525603557; Hm_lpvt_9152f8221cb6243a53c83b956842be8a=1525606057; _jzqb=1.9.10.1525603274.1; _qzja=1.1070225156.1525239298260.1525597069547.1525603274282.1525605398368.1525606071025.0.0.0.86.8; _qzjb=1.1525603274282.9.0.0.0; _qzjto=23.2.0\r\n\r\n'.encode())

	first = True
	buffs = ''
	while 1:
		chunk = sock.recv(1024000)
		if not chunk:
			break
		if first:
			index = chunk.find(b'\r\n\r\n')+len('\r\n\r\n')

			chunk = chunk[index:]
			first = False
		import pdb;pdb.set_trace()
		index = chunk.find(b'\r\n')
		chunk = chunk[index + len('\r\n'):]
		try:
			buffs += chunk.decode("utf-8")
		except:
			import pdb;pdb.set_trace()


		# print(datas[:100])
		# buff = BytesIO(datas)

		# f = gzip.GzipFile(fileobj=buff)

		# res = f.read().decode('utf-8')
		# print(datas)
	with open("test.html", "w") as fp:
		fp.write(buffs)

run()
