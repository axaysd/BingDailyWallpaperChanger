import os
import requests
import re
import win32con, win32gui
import xml.etree.ElementTree as ET

def download_wallpaper():
    xml_url = "http://www.bing.com/HPImageArchive.aspx?format=xml&idx=0&n=1&mkt=en-RU"
    r_xml = requests.get(xml_url)
    with open('bing_xml.xml', 'wb') as f_xml:
        f_xml.write(r_xml.content)
    tree = ET.parse('bing_xml.xml')
    root = tree .getroot()
    imgname_xml = root[0][5].text
    nameArr = re.findall(r'(.*?)\(.*?\)', imgname_xml)
    img_name = ''.join(nameArr) + '.jpg'
    sub_url = root[0][3].text
    img_url = "http://bing.com" + sub_url
    r_img = requests.get(img_url)
    path_to_imgdir = r"C:\Daily Bing Wallpapers"
    if not os.path.exists(path_to_imgdir):
        os.makedirs(path_to_imgdir)
    path_to_img = path_to_imgdir+"\\"+img_name
    with open(path_to_img, 'wb') as f_img:
        f_img.write(r_img.content)
    win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, path_to_img, 3)

def set_wallpaper():
    download_wallpaper()

if __name__=="__main__":
    set_wallpaper()