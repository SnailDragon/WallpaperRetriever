from email.mime import image
import praw
import pprint
import requests
from PIL import Image
import os

reddit = praw.Reddit(client_id='KF-U6QbK3EMpmlAu5o5qsA', client_secret='fT1KeNPdtLcQZXO_5qYpVhB6jocf_g', user_agent='WallpaperScraper')

def scrapeReddit(subreddit, numImages, min_width, min_height, savepath):
    top_posts = reddit.subreddit(subreddit).top(limit=numImages)

    # for post in top_posts:
    #     print(post.title)

    image_posts = []

    for post in top_posts:
        url = post.url
        if((url.find("jpg") >= 0 or url.find("jpeg") >= 0 or url.find("png") >= 0)
            and (url.find("redd.it") >= 0 or url.find("imgur") >= 0)):
            image_posts.append(post)
    if not os.path.exists(savepath):
        os.mkdir(savepath)

    for post in image_posts:
        print(post.url)
        img_data = requests.get(post.url).content
        filetype = post.url[post.url.rfind("."):]
        filename = post.title.replace(" ","") + filetype
        with open(f"{savepath}/{filename}", "wb") as handler:
            handler.write(img_data)

    files = os.listdir(savepath)

    for f in files:
        img = Image.open(f"{savepath}/{f}")
        width = img.width
        height = img.height

        if(width < min_width and height < min_height):
            os.remove(f"{savepath}/{f}")
            files.remove(f)



