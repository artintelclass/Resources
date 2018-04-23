from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import json
import urllib2
import sys
import time
from PIL import Image
from StringIO import StringIO
import argparse

download_path = "dataset/"

def main(args):
	parser = argparse.ArgumentParser(description='Scrape Google images')
	parser.add_argument('-s', '--search', default='bananas', type=str, help='search term')
	parser.add_argument('-n', '--num_images', default=10, type=int, help='num images to save')
	parser.add_argument('--resize', help='resize images', action='store_true')
	parser.add_argument('--width', default=224, type=int, help='width to resize to')
	parser.add_argument('--height', default=224, type=int, help='height to resize to')
	parser.add_argument('--square', help='only square images', action='store_true')
	parser.add_argument('--all_types', help='download multiple image types as available', action='store_true')
	args = parser.parse_args()

	searchtext = args.search
	num_requested = args.num_images
	resize = args.resize
	square = args.square
	allTypes = args.all_types
	w = args.width
	h = args.height

	number_of_scrolls = num_requested / 400 + 1
	# number_of_scrolls * 400 images will be opened in the browser

	if not os.path.exists(download_path + searchtext.replace(" ", "_")):
		os.makedirs(download_path + searchtext.replace(" ", "_"))

	if(square==True):
		url = "https://www.google.co.in/search?q="+searchtext+"&source=lnms&tbm=isch&tbs=iar:s" # &tbs=iar:S means square
	else:
		url = "https://www.google.co.in/search?q="+searchtext+"&source=lnms&tbm=isch"
	driver = webdriver.Chrome('/Users/aaronsherwood/Documents/Classes/artintelclass/Resources/ImageScrape/chromedriver')
	driver.get(url)

	headers = {}
	headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
	extensions = {"jpg"}
	if (allTypes == True):
		extensions = {"jpg", "jpeg", "png", "gif"}
	img_count = 0
	downloaded_img_count = 0

	for _ in xrange(number_of_scrolls):
		for __ in xrange(10):
			# multiple scrolls needed to show all 400 images
			driver.execute_script("window.scrollBy(0, 1000000)")
			time.sleep(0.2)
		# to load next 400 images
		time.sleep(0.5)
		try:
			driver.find_element_by_xpath("//input[@value='Show more results']").click()
		except Exception as e:
			print "Less images found:", e
			break

	# imges = driver.find_elements_by_xpath('//div[@class="rg_meta"]') # not working anymore
	imges = driver.find_elements_by_xpath('//div[contains(@class,"rg_meta")]')
	print "Total images:", len(imges), "\n"
	for img in imges:
		img_count += 1
		img_url = json.loads(img.get_attribute('innerHTML'))["ou"]
		img_type = json.loads(img.get_attribute('innerHTML'))["ity"]
		print "Downloading image", img_count, ": ", img_url
		try:
			if img_type not in extensions:
				img_type = "jpg"
			req = urllib2.Request(img_url, headers=headers)
			raw_img = Image.open(StringIO(urllib2.urlopen(img_url).read()))

			if (resize == True):
				im_small = raw_img.resize((w, h), Image.ANTIALIAS)
				im_small.save(download_path+searchtext.replace(" ", "_")+"/"+str(downloaded_img_count)+"."+img_type)
			else:
				raw_img.save(download_path+searchtext.replace(" ", "_")+"/"+str(downloaded_img_count)+"."+img_type, quality=95)
			downloaded_img_count += 1
		except Exception as e:
			print "Download failed:", e
			try:
				os.remove(download_path+searchtext.replace(" ", "_")+"/"+str(downloaded_img_count)+"."+img_type, quality=95)
			except Exception as e:
				pass
		finally:
			print
		if downloaded_img_count >= num_requested:
			break

	print "Total downloaded: ", downloaded_img_count, "/", img_count
	driver.quit()

if __name__ == "__main__":
	from sys import argv
	main(argv)
