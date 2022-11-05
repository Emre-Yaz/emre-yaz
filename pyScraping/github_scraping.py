# This program gives github profile photo links of desired usernames. 
# You can enter more than one usernames by seperating them with spaces.
# Modified by Emre-Yaz.


def main():
    import requests
    from bs4 import BeautifulSoup as bs

    github_user = input('Input Github User: ')
    github_user = list(github_user.split(' '))

    for user in github_user:
        url = 'https://github.com/'+ user
        r = requests.get(url)
        soup = bs(r.content,'html.parser')
        profile_image = soup.find('img',{'alt': 'Avatar'})['src']
        print('Profile photo link of ' + user + ': ' + profile_image)

if __name__ == '__main__':
    main()