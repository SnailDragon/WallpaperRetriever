from scrapereddit import Scraper

id = input("Enter Client ID: ")
secret = input("Enter Secret ID: ")

scraper = Scraper(id, secret)

#subreddit, numImages, min_width, min_height, savepath):
subreddit = input("Enter subreddit: ")
numImages = int(input("Count: "))
min_width = int(input("Minimum width: "))
min_height = int(input("Minimum height: "))
savepath = input("Save Folder: ")

print("Scraping... ")

scraper.scrapeReddit(subreddit, numImages, min_width, min_height, savepath)

print("Done.")