import re, os, shutil
import initial as browser
from urllib.parse import *
from requests import *
from base64 import *
from bs4 import BeautifulSoup as BS
from time import sleep

class Bypasser:
	def __init__(self):
		self.author = "Riordan Pramana"
	def kuyhaa(self, url):
		try:
			url = b64decode(url).decode('utf-8')
		except:
			url = url
		if "post.techtutors.site" in url:
			query = parse_qs(urlsplit(url).query)
			return bytes.fromhex({k: v[0] for k, v in query.items()}['go']).decode("utf-8")
	def pahe(self, url):
		try:
			url = b64decode(url).decode('utf-8')
		except:
			url = url
		if "intercelestial.com" in url:
			browser.get(url)
			try:
				browser.wait('id','generater')
				browser.find('id','generater').click()
			except:
				print()
			browser.wait('id','showlink')
			browser.find('id','showlink').click()
			browser.driver.switch_to.window(browser.driver.window_handles[-1])
			bs = BS(browser.driver.page_source, 'html.parser')
			return bs.find('a', {"class": "btn-prima"})['href']
	def nimegami(self, url):
		try:
			url = b64decode(url).decode('utf-8')
		except:
			url = url
		if "save.mastah.org" in url:
			return b64decode(url.split("#")[1]).decode("utf-8")
	def gigapurbalingga(self, url):
		try:
			url = b64decode(url).decode('utf-8')
		except:
			url = url
		if "dl.giga74.com" in url:
			query = parse_qs(urlsplit(url).query)
			return b64decode({k: v[0] for k, v in query.items()}['site']).decode("utf-8")
	def oploverz(self, url):
		try:
			url = b64decode(url).decode('utf-8')
		except:
			url = url
		if "hexafile.net" in url:
			req = get(url).text
			return req.split('(countdown);$("a.redirect").attr("href","')[1].split('").html')[0]

	def terbit21(self, url, judul = ""):
		s = Session()
		try:
			url = b64decode(url).decode('utf-8')
		except:
			url = url
		if "https://gfqqqstbtpetpzhw8q2mjfr3kkewste8x9kprthc7a54zuqsnm.xyz" in url:
			req = s.get(url).text
			try:
				url_api = req.split("$.post('")[1].split("', function(res)")[0]
			except:
				return None
			api = s.post("https://gfqqqstbtpetpzhw8q2mjfr3kkewste8x9kprthc7a54zuqsnm.xyz"+url_api).json()['data']
			# callback = []
			# for i,x in enumerate(api):
			# 	callback.append({"file" : s.get(x['file'], allow_redirects = False).headers['Location'], "label" : x['label']})
			return api
		elif "search" in url and judul != "":
			url = "https://nontonfilm.watch/wp-admin/admin-ajax.php?action=muvipro_core_ajax_search_movie&query=" + judul
			return s.post(url).json()
		elif "get_link" in url and judul != "":
			req = s.get("https://terbit21.cool/get/?movie="+judul).text
			bs = BS(req, 'html.parser')
			url_download = bs.find('a', {"id" : "downloadbutton"})['href']
			req = s.post("https://t21.press//verifying.php?movie=" + judul, data = {"movie" : judul}, headers = {"Referer" : url_download}).text
			split = req.split('<div class="table-responsive">')
			table = '<div class="table-responsive">' + split[1].split("</table>")[0] + '</table></div><div class="table-responsive">' + split[2]
			return table.replace('<table width="100%">', '<table width="100%" class="table table-stripped table-hover">')
		elif "get_link_cli" in url and judul != "":
			req = s.get("https://terbit21.cool/get/?movie="+judul).text
			bs = BS(req, 'html.parser')
			url_download = bs.find('a', {"id" : "downloadbutton"})['href']
			req = s.post("https://t21.press//verifying.php?movie=" + judul, data = {"movie" : judul}, headers = {"Referer" : url_download}).text
			return req

class BatchDownloader:
	def __init__(self):
		self.author = "Riordan Pramana"
	def mediafire(self, data):
		download = []
		s = Session()
		if not isinstance(data, list):
			data = [data]
		shutil.rmtree('tmp', ignore_errors = True)
		if os.path.isfile("mediafire.zip"):
			os.remove("mediafire.zip")
		os.mkdir("tmp")
		for c in data:
			req = s.get(c).text
			bs = BS(req, 'html.parser')
			df = bs.find("a", {"class" : "popsok"})["href"]
			with open("tmp/" + df.split("/")[-1].replace("+"," ").split("?")[0], "wb") as mf:
				mf.write(s.get(df).content)
				mf.close()
		shutil.make_archive("mediafire", "zip", "tmp/")
		if os.path.isfile("mediafire.zip"):
			return True
		return None
	def mediafire_cli(self, data, folder):
		download = []
		s = Session()
		req = s.get(data).text
		bs = BS(req, 'html.parser')
		df = bs.find("a", {"class" : "popsok"})["href"]
		try:
			with open(folder + "/" + df.split("/")[-1].replace("+"," ").split("?")[0], "wb") as mf:
				mf.write(s.get(df).content)
				mf.close()
			return "[+] Success Download %s" % df.split("/")[-1].replace("+"," ").split("?")[0]
		except:
			return "[!] Failed Download %s" % df.split("/")[-1].replace("+"," ").split("?")[0]
# b = Bypasser()
# print(b.adfly("http://raboninco.com/19xtZ"))
# print(b.pahe("https://intercelestial.com/?id=MFhQT3JMdzlFWHcxSnVjdTFkeHIvS3JmSGpTcFN4dWo1NnArclV5bE1HWkw0eDRmOU1uNDVGdE9GNUtxU1RiWWsvZ0lVTTZsLzFWcVNDSHVmM09Rc1E9PQ=="))
# print(b.nimegami("http://save.mastah.org/#aHR0cHM6Ly9maWxlcy5pbS8wYmQ0cjVlZ2JxZDY="))
# print(b.gigapurbalingga("http://dl.giga74.com/?site=aHR0cHM6Ly93d3cyNi56aXBweXNoYXJlLmNvbS92L3J4N1labjRNL2ZpbGUuaHRtbA==&c=0&user="))
# print(b.oploverz("https://hexafile.net/K6Oxj"))
# inp = input("Cari Film : ")
# film = b.terbit21("search",inp)['results']
# for i, f in enumerate(film):
# 	print("%s. %s" % (str(i+1), f['title']))
# select = int(input("Pilih Nomor : "))

# print(b.terbit21("https://gfqqqstbtpetpzhw8q2mjfr3kkewste8x9kprthc7a54zuqsnm.xyz/f/1l9654q5lo5/9a625c63922864914a5469d1640ab2bd77638c679df4244a9819d93cc6ef85d83fa149e870f2b8c9fdff24927eb481a733539b3dd1e80c3a9fdc000278162490ca486ff1651722b5506976f91533ba8620429e43e54ff9e7e774e995eeda2e09e4ed2aad097e9aaf2235ac1c27deda8a83de686252a8719f4b573881d3d0673db7f163375fe09b4dbc2d1a6a230ce7f3eafdd5a44499358e7de2e6c05552ec3100fe09fc802a5d56deb8d1543f7ca928bff6507a9b99abd7cfd16b18fd97d8415ad9878cf242630a5d76c0da3c3437b82817fff2b94133d23d60a98763c19e5b6764890a970125f906de18fa75ae26b8f04f0798ea0d4643ede9956cb4e8fcc5599d6b9e08f982fd9652046843a19aab435c0cbd847936952793a67f05cc48491443d9f4fb0510d152790dca9e0780b6cd6072a451287ea12b98f265e603e29ec26234cfbeefc0099b7fd15e696c2dfb8221ec6820c556722cb5e5aa6715bb80b7ae29c02295023efe05aa4f35ac3f69ee4dd2ccf85ffc3386047f63b9e246af62cd8226838419f3def1f0bab86380cc4aff087e3bae10affe9e561c32774feb2b5e866841ccd71afd0d8df4a0f8eadda980e97415cf2e4cf400da8e52d0fc1b45a60022749e84897e2772c79e4ce83fcaa3f3529dc4affbd2517fa295f00ea1834540e2877731af297a0de9d85ac798b1a79055821a18510f36100cbf21c9a44e2f61684f976d8d6d1b2371eefae891b0ab801ef5f3c3a53afe475c5f87c4c558474bddb462a41a9516e1bff2886bf24c4f989b151a6e466c6b4fcc2459a64778b9842251af0d85f134d5974e001c7e1710c6bf164fe9bc44b698736480496c9c0163d5de8393a2369f54c1257b3a9a698df90c99a5cc6209cbf7ed86aadf7089ddf4e8d41542c23625c746a220db59fb8ec188a21cccab69942ed2182d9448cd0c8a99e4851ca8a1fccbdae544f5c6e5bcb8c0c9ba60f8e9976d40cb02b4fd7520173e6d1f1509340088b24efab5a5634e04e3d0ca179eb5009f314d4c19ebd2b7127e55eab2f94ace6e0cb379e24fcf514ddd4b54a9610fa5a165b5ba918a3eb70300d3dac4dcf5bbef84ac188523e76018cc4df8453ed1a62c59725e39499f1cd1d6feba483c89f1ced74c2fcc581ca267c04919bf0c7c717a0b190a717cca8b3894778fb66d30c1523c5958905c2ec8ec3c10d6a14a9623c45063f609e3344a4c246ac704aaef3c3328abbf70020e8a7f0f1b40bfa6f1b02e5ad556647059bc8252858b8ae384ad4a0cc94b119202136f5f0ee30e08123ccb28c7fd41c6636f49833775935f07b4ee7c13afaeb86f369e5921a740698909cd3dfea39b279babee86d3f19ab2459953104c3f2c0089d5cc64e9f57fdcf63636266f286892adeaab2d9e3f9d73ae9b3774253c25ba2571c771b6aebb27125031b5aa123b.mp4"))
# b = Batch()
# b.mediafire("https://www.mediafire.com/file/c871asccjol1dd3/welcome_to_mobile_entod.mp3/file?fbclid=IwAR23PmS49XfoYlo2UjRzO6-awXAUd_gxCz_lGRV4hJRCSXfbJB_bUGGnGHM")