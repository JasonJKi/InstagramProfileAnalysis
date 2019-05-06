import json
from InstagramAPI import InstagramAPI
from InstaAnalyticTools import UserInfoGenerator

with open('../.credential/instagram.txt') as json_file:
    credential = json.load(json_file)

my_user_name = credential["username"]
password = credential["password"]

api = InstagramAPI(**credential)
api.login()

# get data 
user_name = "dr.johnyoo"
user = UserInfoGenerator(user_name)
user_id = user.getUserID()
users_followers = user.get_public_followers(user_id, api)
num_followers = len(users_followers['username'])
print(num_followers)


data_dir = '../data/user/'
scraper = user.scraper
scraper.usernames=users_followers['username'][:100]
scraper.scrape(file_dir=data_dir)
matching = [s for s in users_followers['username'] if "jason.j.ki" in s]

