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
  #1
  "https://www.dropbox.com/sh/bz7m50royjbm419/AABVnP0iqtsCmFGLOWpfTukca/%D7%A7%D7%95%D7%A8%D7%A1%20%D7%A4%D7%95%D7%98%D7%95%D7%A9%D7%95%D7%A4%20%D7%90%D7%95%D7%92%D7%95%D7%A1%D7%98%20-%20%D7%A9%D7%99%D7%A2%D7%95%D7%A8%201%2016-8-20-1.mp4?dl=0",
  "https://www.dropbox.com/sh/bz7m50royjbm419/AAAdnU5_MKDoGimui4InrljSa/%D7%A7%D7%95%D7%A8%D7%A1%20%D7%A4%D7%95%D7%98%D7%95%D7%A9%D7%95%D7%A4%20%D7%90%D7%95%D7%92%D7%95%D7%A1%D7%98%20-%20%D7%A9%D7%99%D7%A2%D7%95%D7%A8%201%2016-8-20-2.mp4?dl=0",
  "https://www.dropbox.com/sh/bz7m50royjbm419/AAD12lvceNphhnM9T25LX2Xna/%D7%A7%D7%95%D7%A8%D7%A1%20%D7%A4%D7%95%D7%98%D7%95%D7%A9%D7%95%D7%A4%20%D7%90%D7%95%D7%92%D7%95%D7%A1%D7%98%20-%20%D7%A9%D7%99%D7%A2%D7%95%D7%A8%201%2016-8-20-3.mp4?dl=0",
  "https://www.dropbox.com/sh/bz7m50royjbm419/AABDbQVa1qGdHNtIgq9cZ2bGa/%D7%A7%D7%95%D7%A8%D7%A1%20%D7%A4%D7%95%D7%98%D7%95%D7%A9%D7%95%D7%A4%20%D7%90%D7%95%D7%92%D7%95%D7%A1%D7%98%20-%20%D7%A9%D7%99%D7%A2%D7%95%D7%A8%201%2016-8-20-4.mp4?dl=0",
  #2
  "https://www.dropbox.com/sh/gwxgp11o9qkxsdj/AAB9J1nAvqWWrXjF_KBbMPn_a/%D7%A7%D7%95%D7%A8%D7%A1%20%D7%A4%D7%95%D7%98%D7%95%D7%A9%D7%95%D7%A4%20%D7%90%D7%95%D7%92%D7%95%D7%A1%D7%98%20-%20%D7%A9%D7%99%D7%A2%D7%95%D7%A8%202%2023-8-20-1.mp4?dl=0",
  "https://www.dropbox.com/sh/gwxgp11o9qkxsdj/AADrGou2AJBXRzAZ3SKkirHRa/%D7%A7%D7%95%D7%A8%D7%A1%20%D7%A4%D7%95%D7%98%D7%95%D7%A9%D7%95%D7%A4%20%D7%90%D7%95%D7%92%D7%95%D7%A1%D7%98%20-%20%D7%A9%D7%99%D7%A2%D7%95%D7%A8%202%2023-8-20-2.mp4?dl=0",
  "https://www.dropbox.com/sh/gwxgp11o9qkxsdj/AAC4AIJeaPuNG6i50VVo0r_ga/%D7%A7%D7%95%D7%A8%D7%A1%20%D7%A4%D7%95%D7%98%D7%95%D7%A9%D7%95%D7%A4%20%D7%90%D7%95%D7%92%D7%95%D7%A1%D7%98%20-%20%D7%A9%D7%99%D7%A2%D7%95%D7%A8%202%2023-8-20-3.mp4?dl=0",
  "https://www.dropbox.com/sh/gwxgp11o9qkxsdj/AADTGL81H7FuFXgTqxEiUHbua/%D7%A7%D7%95%D7%A8%D7%A1%20%D7%A4%D7%95%D7%98%D7%95%D7%A9%D7%95%D7%A4%20%D7%90%D7%95%D7%92%D7%95%D7%A1%D7%98%20-%20%D7%A9%D7%99%D7%A2%D7%95%D7%A8%202%2023-8-20-4.mp4?dl=0",
  #3
  "https://www.dropbox.com/sh/6kae3y2346phaxj/AABqTXiNjDH2-7NArqSWCNOKa/%D7%A7%D7%95%D7%A8%D7%A1%20%D7%A4%D7%95%D7%98%D7%95%D7%A9%D7%95%D7%A4%20%D7%90%D7%95%D7%92%D7%95%D7%A1%D7%98%20-%20%D7%A9%D7%99%D7%A2%D7%95%D7%A8%203%20-%2030.08-1.mp4?dl=0",
  "https://www.dropbox.com/sh/6kae3y2346phaxj/AAALDpz1qv7MJ1UIZg7t7V0Pa/%D7%A7%D7%95%D7%A8%D7%A1%20%D7%A4%D7%95%D7%98%D7%95%D7%A9%D7%95%D7%A4%20%D7%90%D7%95%D7%92%D7%95%D7%A1%D7%98%20-%20%D7%A9%D7%99%D7%A2%D7%95%D7%A8%203%20-%2030.08-2.mp4?dl=0",
  "https://www.dropbox.com/sh/6kae3y2346phaxj/AAAqpr2PAQmImaS9IwHw5Uhwa/%D7%A7%D7%95%D7%A8%D7%A1%20%D7%A4%D7%95%D7%98%D7%95%D7%A9%D7%95%D7%A4%20%D7%90%D7%95%D7%92%D7%95%D7%A1%D7%98%20-%20%D7%A9%D7%99%D7%A2%D7%95%D7%A8%203%20-%2030.08-3.mp4?dl=0",
  #4
  "https://www.dropbox.com/sh/8gv1i5e60ts1sz5/AAClzxJhHlzSGxQHsgqhBjTIa/%D7%A4%D7%95%D7%98%D7%95%D7%A9%D7%95%D7%A4%20-%20%D7%A9%D7%99%D7%A2%D7%95%D7%A8%204%20-%206.09-1.mp4?dl=0",
  "https://www.dropbox.com/sh/8gv1i5e60ts1sz5/AAB79VvPpUrFuQfX7vZujzJWa/%D7%A4%D7%95%D7%98%D7%95%D7%A9%D7%95%D7%A4%20-%20%D7%A9%D7%99%D7%A2%D7%95%D7%A8%204%20-%206.09-2.mp4?dl=0",
  "https://www.dropbox.com/sh/8gv1i5e60ts1sz5/AAD0aDQs2nOVDW65TDSLGO7ma/%D7%A4%D7%95%D7%98%D7%95%D7%A9%D7%95%D7%A4%20-%20%D7%A9%D7%99%D7%A2%D7%95%D7%A8%204%20-%206.09-3.mp4?dl=0",
  #5
  "https://www.dropbox.com/sh/05ywklo0e8micmn/AACn3vSBZ6pxN6BGYQyvbOsqa/%D7%A4%D7%95%D7%98%D7%95%D7%A9%D7%95%D7%A4%20-%20%D7%A9%D7%99%D7%A2%D7%95%D7%A8%205%20-%2013.09-1.mp4?dl=0",
  "https://www.dropbox.com/sh/05ywklo0e8micmn/AABvfBAoDjWjY-srm_r3UgqOa/%D7%A4%D7%95%D7%98%D7%95%D7%A9%D7%95%D7%A4%20-%20%D7%A9%D7%99%D7%A2%D7%95%D7%A8%205%20-%2013.09-2.mp4?dl=0",
  "https://www.dropbox.com/sh/05ywklo0e8micmn/AADLd-RDGUjTTVgii5CL9AoJa/%D7%A4%D7%95%D7%98%D7%95%D7%A9%D7%95%D7%A4%20-%20%D7%A9%D7%99%D7%A2%D7%95%D7%A8%205%20-%2013.09-3.mp4?dl=0",
  #6
  "https://www.dropbox.com/sh/d6g2nkz2asyw00b/AAC1S_Z6NW-P1Zkwvi2DHwENa/%D7%A4%D7%95%D7%98%D7%95%D7%A9%D7%95%D7%A4%20-%20%D7%A9%D7%99%D7%A2%D7%95%D7%A8%206%20-%2023.09-1.mp4?dl=0",
  "https://www.dropbox.com/sh/d6g2nkz2asyw00b/AABXuFlLd5AtDl621g-r7kQGa/%D7%A4%D7%95%D7%98%D7%95%D7%A9%D7%95%D7%A4%20-%20%D7%A9%D7%99%D7%A2%D7%95%D7%A8%206%20-%2023.09-2.mp4?dl=0",
  "https://www.dropbox.com/sh/d6g2nkz2asyw00b/AADSd48J89SqDT-cm_tj8wUpa/%D7%A4%D7%95%D7%98%D7%95%D7%A9%D7%95%D7%A4%20-%20%D7%A9%D7%99%D7%A2%D7%95%D7%A8%206%20-%2023.09-3.mp4?dl=0",
  #7
  "https://www.dropbox.com/sh/6974r412iilnq12/AACfX3FHii2tXdIkF0m8y_pHa/%D7%A4%D7%95%D7%98%D7%95%D7%A9%D7%95%D7%A4%20-%20%D7%A9%D7%99%D7%A2%D7%95%D7%A8%207%20-29.09-1.mp4?dl=0",
  "https://www.dropbox.com/sh/6974r412iilnq12/AAD8VnCcFZs5kL0DfIuCKj5va/%D7%A4%D7%95%D7%98%D7%95%D7%A9%D7%95%D7%A4%20-%20%D7%A9%D7%99%D7%A2%D7%95%D7%A8%207%20-29.09-2.mp4?dl=0",
  "https://www.dropbox.com/sh/6974r412iilnq12/AACsyxmPAXtgnprXGYNcXy_La/%D7%A4%D7%95%D7%98%D7%95%D7%A9%D7%95%D7%A4%20-%20%D7%A9%D7%99%D7%A2%D7%95%D7%A8%207%20-29.09-3.mp4?dl=0",
  #8
  "https://www.dropbox.com/sh/junqf0r3o1qkmdc/AAAtFnnofIm-4EvV9AHrhlNTa/%D7%A4%D7%95%D7%98%D7%95%D7%A9%D7%95%D7%A4%20-%D7%A9%D7%99%D7%A2%D7%95%D7%A8%208%20-11.10-1.mp4?dl=0",
  "https://www.dropbox.com/sh/junqf0r3o1qkmdc/AAAYeaqkXzrqG5FY-PtdD8TJa/%D7%A4%D7%95%D7%98%D7%95%D7%A9%D7%95%D7%A4%20-%D7%A9%D7%99%D7%A2%D7%95%D7%A8%208%20-11.10-2.mp4?dl=0",
  "https://www.dropbox.com/sh/junqf0r3o1qkmdc/AAAwuXXvB259PEHVsOPvqPbYa/%D7%A4%D7%95%D7%98%D7%95%D7%A9%D7%95%D7%A4%20-%D7%A9%D7%99%D7%A2%D7%95%D7%A8%208%20-11.10-3.mp4?dl=0",
  "https://www.dropbox.com/sh/junqf0r3o1qkmdc/AAC0TjtVdL4JHywE8IKnU9dRa/%D7%A4%D7%95%D7%98%D7%95%D7%A9%D7%95%D7%A4%20-%D7%A9%D7%99%D7%A2%D7%95%D7%A8%208%20-11.10-4.mp4?dl=0"
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


