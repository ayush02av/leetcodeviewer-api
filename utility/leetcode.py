import requests
        
def get_leetcode_details_from_username(username):
    url = "https://leetcode.com/graphql/"
    body = """
    {
        matchedUser(username: "%s") {
            username
            githubUrl
            twitterUrl
            linkedinUrl
            profile: profile{
                reputation
                aboutMe
                websites
                ranking
                userAvatar
                realName
                countryName
            }
            languageStats: languageProblemCount{
                languageName
                problemsSolved
            }
            skillStats: tagProblemCounts{
                advanced{
                    tagName
                    tagSlug
                    problemsSolved
                }
                intermediate{
                    tagName
                    tagSlug
                    problemsSolved
                }
                fundamental{
                    tagName
                    tagSlug
                    problemsSolved
                }
            }
            submitStats: submitStatsGlobal {
                    acSubmissionNum {
                    difficulty
                    count
                    submissions
                    }
                }
            }
    }
    """ % (username)
    
    response = requests.post(url=url, json={"query": body})

    if response.status_code == 200:
        if 'errors' not in response.json().keys():
            return response.json()['data']['matchedUser']
            
    return None