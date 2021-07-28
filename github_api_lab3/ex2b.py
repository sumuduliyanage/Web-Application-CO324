#E/16/200
#Question 2-part a 


from typing import List, Tuple
import requests
import pprint

def github_superstars(orgnanization: str) -> List[Tuple]:

	with requests.Session() as session:
		session.headers['Authorization'] = 'token ed77e01fbdcc9b54a596e7e366eba88c9cdc251f'#setting authorization
		url = "https://api.github.com/orgs/"+orgnanization+"/members"#getting the url
		response = session.get(url)#takes the response for the request
		jsonres = response.json()#getting json oject
		profiles = list()
		names = list()
		max_stars_list = list() 
    
	   
	for a in jsonres:
		
		names.append(a['login'])#list names have the names of the members
		
		s = a['url']#getting the url of 
		profiles.append(s)#profiles include github urls for the members
		response2 = session.get(s)#getting response for the requests
		jsonob = response2.json()#getting json object
		repo_url = jsonob['repos_url']#repos urls
		response3 = session.get(repo_url+"?page=1&per_page=100")#getting 100 repos per page
		public_repos = response3.json()#json objects
		
		
		user_repos = list()#new list of repos
			
		for repo in public_repos:
			repo_name = repo['name']
			owner = repo['owner']['login']
			url_repo_users = 'https://api.github.com/repos/'+owner+'/'+repo_name
			repo_info = session.get(url_repo_users)
			stars = repo_info.json()['stargazers_count']#getting no of stars for a particular repo
			user_repos.append((url_repo_users, stars))
			
		user_repos.sort(key = lambda x: x[1] , reverse = True)#sorting all the stars for a person in reverse order
		
		max_stars_list.append(user_repos[0])	
	
	#after they are sorted	
	max_stars_list.sort(key = lambda x: x[1] , reverse = True)	
	
	
	#if you want to print the names of members,uncomment below two lines
	#print(names)
	#print()
	
	return (max_stars_list)
	

x = github_superstars("cepdnaclk")	
winner_superstar_url = x[0]
with requests.Session() as session:
	session.headers['Authorization'] = 'token ed77e01fbdcc9b54a596e7e366eba88c9cdc251f'#setting authorization
session.put(winner_superstar_url[0]+'/subscription')


	






