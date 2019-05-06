import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup
import ssl
import json
from instagram_scraper import InstagramScraper
        
class UserInfoGenerator:

    def __init__(self, user_name=''):
        self.main()
        self.user_name = user_name;
        self.initInstagramScraper(user_name) 
    
    def initInstagramScraper(self, user_name):
        args = {'username':user_name}
        self.scraper = InstagramScraper(**args)
            
    def getUserID(self, user_name=[]):
        if not user_name:
            user_name = self.user_name
        scraper = self.scraper
        USER_ID_REQUEST = 'entry_data.ProfilePage[0].graphql.user'
        user = scraper.deep_get(scraper.get_shared_data(user_name), USER_ID_REQUEST)
        user_id = int(user['id'])
        return user_id
    
    def get_public_followers(self, user_id, api):
        followers = self.getFollowers(user_id, api)
        user_names = []
        user_ids = []
        for user_data in followers:        
            if not user_data['is_private']:
                user_ids.append(user_data['pk']) 
                user_names.append(user_data['username'])
        
        followers = {'id':user_ids,'username':user_names}
        return followers
            
    def getinfo(self, url):
        html = urllib.request.urlopen(url, context=self.ctx).read()
        soup = BeautifulSoup(html, 'html.parser')
        data = soup.find_all('meta', attrs={'property': 'og:description'
                             })
        text = data[0].get('content').split()
        user = '%s %s %s' % (text[-3], text[-2], text[-1])
        followers = text[0]
        following = text[2]
        posts = text[4]
        info={}
        info["User"] = user
        info["Followers"] = followers
        info["Following"] = following
        info["Posts"] = posts
        return info

    def main(self):
        self.ctx = ssl.create_default_context()
        self.ctx.check_hostname = False
        self.ctx.verify_mode = ssl.CERT_NONE


    def read_textfile(self):
        with open('users.txt') as f:
            self.content = f.readlines()
        self.content = [x.strip() for x in self.content]
        for url in self.content:
            self.getinfo(url)
    
    def get_links(self, hashtag, url):

        html = urllib.request.urlopen(url, context=self.ctx).read()
        soup = BeautifulSoup(html, 'html.parser')
        script = soup.find('script', text=lambda t: \
                           t.startswith('window._sharedData'))
        page_json = script.text.split(' = ', 1)[1].rstrip(';')
        data = json.loads(page_json)
        print ('Scraping links with #' + hashtag+"...........")
        for post in data['entry_data']['TagPage'][0]['graphql'
                ]['hashtag']['edge_hashtag_to_media']['edges']:
            image_src = post['node']['thumbnail_resources'][1]['src']
            hs = open(hashtag + '.txt', 'a')
            hs.write(image_src + '\n')
            hs.close()
            
    def getFollowers(self, user_id,  api):
        """
        Returns the list of followers of the user.
        It should be equivalent of calling api.getTotalFollowers from InstagramAPI
        """
        followers = []
        next_max_id = True
        while next_max_id:
            # first iteration hack
            if next_max_id is True:
                next_max_id = ''
    
            _ = api.getUserFollowers(user_id, maxid=next_max_id)
            followers.extend(api.LastJson.get('users', []))
            next_max_id = api.LastJson.get('next_max_id', '')
        return followers

    def getFollowings(user_id,  api):
        """
        Returns the list of followers of the user.
        It should be equivalent of calling api.getTotalFollowers from InstagramAPI
        """
    
        followers = []
        next_max_id = True
        while next_max_id:
            # first iteration hack
            if next_max_id is True:
                next_max_id = ''
    
            _ = api.getUserFollowings(user_id, maxid=next_max_id)
            followers.extend(api.LastJson.get('users', []))
            next_max_id = api.LastJson.get('next_max_id', '')
        return followers

       

if __name__ == '__main__':
    obj = InstaScraper()
    obj.main()