# Outline
##### Pcap檔案 => 轉換為文字檔 => 萃取domain => 算亂度來分出正常和異常domain name

### 前置準備
- 準備好Pcap檔案
- 電腦中安裝python2.7.9

python下載檔案路徑：https://www.python.org/

#### 安裝步驟
![1](安裝python/1.jpg)
![1](安裝python/2.jpg)
![1](安裝python/3.jpg)
#### 環境配置，就是將安裝python的資料夾加入到path中，截圖如下：
![1](安裝python/4path.jpg)
#### python 安裝好後需要另外安裝numpy套件
下載路徑：http://sourceforge.net/projects/numpy/files/NumPy/1.7.0/
![numpy](安裝python/Numerical.jpg)

### Pcap檔案 => 轉換為文字檔
簡易方法：直接用`WIRESHARK`開啟，匯出為`csv`

### 轉換為文字檔 => 萃取domain

- ###### python程式名稱：refile.py
- ###### 執行程式方法：python` `refile.py` `logs.csv
- ###### 注意：此程式只有`針對`於`WIRESHARK`用csv匯出的檔案格式
- ###### 執行完成會有兩個檔案匯出，`twoCategory.txt`和`domainName.txt`


`refile.py`程式如下：

	# -*- coding: UTF-8 -*-
	import re
	import sys

	def appendWrite(filename,data):
		f = open(filename,"a")
		f.write(data)
		f.close
	#sys.argv[1]
		
	if __name__ == "__main__":
		twoCategory = "twoCategory.txt"
		domainName = "domainName.txt"
		f = open(sys.argv[1])
		d = []
		for line in f:
			if "A " and "DNS" in line:
				try:
					data =line.split(",")[0] +","+ line.split(",")[6].split(" ")[5] 
					print data
					data = data[0:-1]
					appendWrite(twoCategory,data+"\n")
					d.append(line.split(",")[6].split(" ")[5])
				except:
					print line
		dd =set(d)
		for line in dd:
			line = line[0:-1]
			appendWrite(domainName,line+"\n")
		f.close

### 萃取domain => 算亂度來分出正常和異常domain name
##### 執行方法：python` `dgascore.py` `domainName.txt 
##### 結果：
	jiankang.wangchao.net.cn. score: 0.000000 perp: 3.05471736861
	clients1.google.com. score: 0.000000 perp: 1.44268838855
	muying.wangchao.net.cn. score: 0.000000 perp: 1.41631415482
	fbstatic-a.akamaihd.net. score: 35.426153 perp: 1.94432644347
	zhubao.wangchao.net.cn. score: 0.000000 perp: 22.9313117664
	zhidao.wangchao.net.cn. score: 0.000000 perp: 22.9313117664
	junshi.wangchao.net.cn. score: 0.000000 perp: 3.38111007693
	accounts.youtube.com. score: 0.000000 perp: 1.14582487754
	accounts.google.com. score: 0.000000 perp: 1.15406357502
	meirong.wangchao.net.cn. score: 0.000000 perp: 1.39504250204
	tansuo.wangchao.net.cn. score: 17.962885 perp: 1.19006470323
	tw.bid.yahoo.com. score: 84.005009 perp: 1.270309482
	sd.symcd.com. score: 38.945323 perp: 1.88950308729
	y.analytics.yahoo.com. score: 40.279493 perp: 4.29963461215
	tw.yimg.com. score: 162.576642 perp: 1.41625399787

##### 解說：
- dgascore.py：是主程式
- domainName.txt：上一個步驟匯出的檔案名稱
- score：分數超過80就可能是異常的網域名稱


---

# pcapToWhiteToWhois.py

> 預先工作：要將whois套件安裝。可參考：https://code.google.com/p/pywhois/。
> 之前環境設定都正確的話，在命令提示字元中加入直接打入 pip install python-whois

### 準備`pcap`檔案利用`whireshark`匯出csv

### 此檔案可以將`csv`匯出三個檔案
1. domainName.txt：將csv裡面只挑選出domain name
2. whiteListFilter.txt：透過`www.alexa.com`公開的受歡迎網站來過濾出有可能異常的網頁
3. queryWhois.txt：利用python的whois呼叫，並將檔案格式標準化為json


### 四個檔案的格式範例：
##### 匯出的csv檔案格式
	"No.","Time","Source","Destination","Protocol","Length","Info"
	"51","0.149659000","fe80::b5e6:ab10:6bd3:492","ff02::1:3","LLMNR","84","Standard query 0x0472  A wpad"
	"52","0.149660000","140.138.149.76","224.0.0.252","LLMNR","64","Standard query 0x0472  A wpad"
	"62","0.249950000","fe80::b5e6:ab10:6bd3:492","ff02::1:3","LLMNR","84","Standard query 0x0472  A wpad"
	"63","0.249951000","140.138.149.76","224.0.0.252","LLMNR","64","Standard query 0x0472  A wpad"
	"127","0.736938000","140.138.148.138","140.138.2.109","DNS","102","Standard query 0x9d85  A cqi25izlyk27jtpta47fzgqb38mumuh54ktaw.info"

#### domainName.txt

	s.ytimg.com
	bthui35aqp42isiuitc49iyiwj66owc29pwgv.biz
	ixivd40n20bxeya17d30friugvjyetn40l58a17.info
	ovksc29h24e21gsp62asl38gxo11b48hsk67fzhw.com
	lrayi65hxbta67kzk37c49kxm19psksl58hqgx.ru
	h34nzfwo21fqgua27bzcsf52mxcyn20k57a67fs.biz

#### whiteListFilter.txt

	s.ytimg.com
	bthui35aqp42isiuitc49iyiwj66owc29pwgv.biz
	ixivd40n20bxeya17d30friugvjyetn40l58a17.info
	ovksc29h24e21gsp62asl38gxo11b48hsk67fzhw.com
	lrayi65hxbta67kzk37c49kxm19psksl58hqgx.ru
	h34nzfwo21fqgua27bzcsf52mxcyn20k57a67fs.biz
	krk17krb58ltoskufyh14owi45drjwhqesgy.biz

#### queryWhois.txt

	{'status': 1, 'domain_name': ['YTIMG.COM', 'ytimg.com'], 'creation_date': '2007-12-11T00:00:00', 'whois_server': ['whois.markmonitor.com', 'whois.markmonitor.com'], 'input_domain': 's.ytimg.com', 'registrar': ['MARKMONITOR INC.', 'MarkMonitor, Inc.'], 'name_servers': ['NS1.GOOGLE.COM', 'NS2.GOOGLE.COM', 'NS3.GOOGLE.COM', 'NS4.GOOGLE.COM', 'ns1.google.com', 'ns2.google.com', 'ns4.google.com', 'ns3.google.com']}
	{'status': 0, 'input_domain': 'bthui35aqp42isiuitc49iyiwj66owc29pwgv.biz'}
	{'status': 0, 'input_domain': 'ixivd40n20bxeya17d30friugvjyetn40l58a17.info'}
	{'status': 0, 'input_domain': 'ovksc29h24e21gsp62asl38gxo11b48hsk67fzhw.com'}
	{'status': 0, 'input_domain': 'lrayi65hxbta67kzk37c49kxm19psksl58hqgx.ru'}
	{'status': 0, 'input_domain': 'h34nzfwo21fqgua27bzcsf52mxcyn20k57a67fs.biz'}


### 執行方法： python pcapToWhiteToWhois.py tran.csv 
* 執行方式是用空格分隔來指定tran.csv檔案就可