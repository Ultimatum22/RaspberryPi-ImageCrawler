import os
import sys
import socket
import shutil
import platform
from hashlib import md5
from urllib2 import urlopen
from urllib import urlretrieve
#import selenium.webdriver as webdriver
from BeautifulSoup import BeautifulSoup


"""class ImageCrawler():
    REMOTE_SERVER = "www.google.com"




    def __init__(self, working_directory):
        if self.is_connected():
            self.images_output_folder = os.path.join(working_directory, "images")
            self.chromedriver = os.path.join(working_directory, "chromedriver")

            if not os.path.exists(self.images_output_folder):
                os.makedirs(self.images_output_folder)

            self.urls = []
            self.urls.append("http://www.deviantart.com/?order=67108864&offset=0")
            self.urls.append("http://www.pinterest.com/sylvesterhiew/hipster-quotes/")
            self.urls.append("http://www.pinterest.com/all/technology/")
            self.urls.append("http://www.instagram.com/apeacefulwarrior1")

            for url in self.urls:
                if url.startswith("http://www.deviantart.com/"):
                    self.find_images_deviantart(url)
                elif url.startswith("http://www.pinterest.com/"):
                    self.find_images_pinterest(url)
                elif url.startswith("http://www.instagram.com/"):
                    self.find_images_instagram(url)

    def find_images_deviantart(self, url):
        #driver = self.get_chromedriver(url)
        #soup = BeautifulSoup(driver.page_source)
        soup = BeautifulSoup(urlopen(url))

        browse_results = soup.find(id="browse-results")
        for link in browse_results.findAll("a"):
            super_full_img = link.get("data-super-full-img")
            if super_full_img is not None:
                self.download_image(super_full_img)
            else:
                super_img = link.get("data-super-img")
                if super_img is not None:
                    self.download_image(super_img)

        #driver.close()

    def find_images_pinterest(self, url):
        #driver = self.get_chromedriver(url)
        #driver = self.get_chromedriver(url)
        #soup = BeautifulSoup(driver.page_source)
        soup = BeautifulSoup(urlopen(url))

        for link in soup.findAll("img"):
            if link.get("src").startswith("http://media-cache-ec0.pinimg.com/236x"):
                image = link.get("src").replace("236x", "736x")
                self.download_image(image)

        #driver.close()

    def find_images_instagram(self, url):
        print "Instagram"

        #driver = self.get_chromedriver(url)
        soup = BeautifulSoup(urlopen(url))

        for x in soup.findAll('li', {'class':'photo'}):
            print x

        #driver.close()

    def download_image(self, image_url):
        filename, extension = os.path.splitext(image_url)
        hashed_filename = md5(filename.split("/")[-1]).hexdigest() + extension
        path = os.path.join(self.images_output_folder, hashed_filename)

        if not os.path.exists(path):
            urlretrieve(image_url, path)
            print "Downloading image: %s" % image_url

    def get_chromedriver(self, url):
        driver = None
        if platform.system() == "Linux":
            driver =  webdriver.Chrome(executable_path="/home/pi/media/chromedriver/chromedriver")
        elif platform.system() == "Windows":
            driver = webdriver.Chrome(executable_path=self.chromedriver +"/chromedriver.exe")

        if driver is not None:
            driver.get(url)
            return driver

    def is_connected(self):
        try:
            # see if we can resolve the host name -- tells us if there is
            # a DNS listening
            host = socket.gethostbyname(self.REMOTE_SERVER)
            # connect to the host -- tells us if the host is actually
            # reachable
            socket.create_connection((host, 80), 2)
            return True
        except:
            pass
            return False

if __name__ == '__main__':
    ImageCrawler(sys.argv[-1])"""