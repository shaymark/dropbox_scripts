# go to video link page

# go to source code

# find the 720 p url

# with vlc cmdline convert the file to mp4 file

import urllib.request as urllib2
import subprocess
import uuid

#url = "https://www.dropbox.com/sh/0w65g0z59iigqn1/AAAYWJwxrseZDRX8gEHULxYJa?dl=0&preview=%D7%A4%D7%95%D7%98%D7%95%D7%A9%D7%95%D7%A4+-+%D7%A9%D7%99%D7%A2%D7%95%D7%A8+9+-18.10-4.mp4"

#videoUrl = "https://uc0c7aad4b32e43e591a95f28287.previews.dropboxusercontent.com/p/hls_master_playlist/AA_9UnVPoL7gDz807Cb-FMBNsYexgc5dksEFzKkAfgsyvpGZFHn5DwwOuOBnY6BUs9GTPWxOCHDNbG3D6yVUVd5Hur445bc4KsBRPNfkcC_AOuSqbZP_BWXz9SUjvS1f5w4LzrJ5TWjR7KabRATDd4Ix8c8cHGZUX4X1IDnVZA_KL6AaHLsGSWPkWPfdjMau3GAc7HehTPJGqGApc2rnEchu1PB70BM-4ismf7GZCUuDVt9i5v6_0E2RzK44z2NORnig0BGlebgH6IUxYBCH2kL7gCg7Gso5OLRAN0I8NlASWZOsMdAcQFC_lPthTEPP7jA/p.m3u8"

urlList = [
  "https://www.dropbox.com/sh/0w65g0z59iigqn1/AAAYWJwxrseZDRX8gEHULxYJa?dl=0&preview=%D7%A4%D7%95%D7%98%D7%95%D7%A9%D7%95%D7%A4+-+%D7%A9%D7%99%D7%A2%D7%95%D7%A8+9+-18.10-1.mp4",
  "https://www.dropbox.com/sh/0w65g0z59iigqn1/AAAYWJwxrseZDRX8gEHULxYJa?dl=0&preview=%D7%A4%D7%95%D7%98%D7%95%D7%A9%D7%95%D7%A4+-+%D7%A9%D7%99%D7%A2%D7%95%D7%A8+9+-18.10-2.mp4",
  "https://www.dropbox.com/sh/0w65g0z59iigqn1/AAAYWJwxrseZDRX8gEHULxYJa?dl=0&preview=%D7%A4%D7%95%D7%98%D7%95%D7%A9%D7%95%D7%A4+-+%D7%A9%D7%99%D7%A2%D7%95%D7%A8+9+-18.10-3.mp4",
  "https://www.dropbox.com/sh/0w65g0z59iigqn1/AAAYWJwxrseZDRX8gEHULxYJa?dl=0&preview=%D7%A4%D7%95%D7%98%D7%95%D7%A9%D7%95%D7%A4+-+%D7%A9%D7%99%D7%A2%D7%95%D7%A8+9+-18.10-4.mp4"
]

def printToFile(fileName, text):
  f = open(fileName, "w")
  f.write(text)
  f.close()

def getUrlContent(url):
  response = urllib2.urlopen(url)
  html = response.read()
  return html

def getVideoUrl(html, type):
  prefix = "720p\":"
  prefixIndex = html.find(prefix)
  print(prefixIndex)
  urlStartIndex = html.find("\"", prefixIndex + len(prefix)) + 1
  print(urlStartIndex)
  urlEndIndex = html.find("\"", urlStartIndex)
  print(urlEndIndex)
  return html[urlStartIndex: urlEndIndex]

def getVlcParmeters(videoUrl, dstFile):
  vlc = r"C:\Program Files\VideoLAN\VLC\vlc.exe"
  return [vlc, videoUrl, "--sout" , '#transcode{vcodec=h264,ab=70,channels=2,samplerate=44100}:std{access=file,mux=mp4,dst=' + dstFile + '}', 'vlc://quit']

def convertVideoFile(videoUrl, dstFile):
  vlcParameters = getVlcParmeters(videoUrl, dstFile)
  p = subprocess.Popen(vlcParameters)
  p.wait()

def convertUrl(url, destFileName):
  body = str(getUrlContent(url))
  printToFile("body.txt", body)
  videoUrl = getVideoUrl(body, "p")
  print (videoUrl)
  convertVideoFile(videoUrl, destFileName)

i=1
uuid =  str(uuid.uuid4())
for url in urlList:
  convertUrl(url, str(i) + "_" + uuid + ".mp4")
  i = i + 1


