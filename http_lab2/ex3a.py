from urllib import request
from json import loads
from typing import List, Dict
import json
import requests

#part a - question 3
def ddg_query(url: str, nr_results: int) -> List[str]:
    
    name_list = list()
    results_list = list()
    related_topics_list = list()

    #splitting by space
    name_list = url.strip().split()
    url_name = "+".join(name_list)#joining them with+

    #whole url 
    url_name = "https://www.duckduckgo.com/?q="+url_name+"&format=json&pretty=1"

    #requesting
    with request.urlopen(url_name) as query:
        
        body = query.read().decode('utf-8')
        json_body = json.loads(body)

        for result in json_body['Results']:#getting results
            results_list.append(result['FirstURL'])

        for related_topic in json_body['RelatedTopics']:#getting related topics
            related_topics_list.append(related_topic['FirstURL'])

        URLS = results_list + related_topics_list#joing them together

        if (nr_results > len(URLS)):#if they are asking more than exists
            return URLS

        return (URLS[:nr_results])


#for part a - search for an item
print (ddg_query("University Of Peradeniya",1))
print()
