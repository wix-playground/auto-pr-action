import requests

GITHUB_API = 'https://api.github.com'

def get_commit(owner, repo, ref, token):
    url = f'{GITHUB_API}/repos/{owner}/{repo}/commits/{ref}'
    print(url)
    
    headers = {"Authorization": f"Bearer {token}"}
   
    response = requests.get(url, headers=headers)
    print("response:", response)

    if response.status_code != requests.codes.ok:
        return {}
    
    return response.json()


def get_prs_for(owner, repo, branch, token):
    url = f'{GITHUB_API}/repos/{owner}/{repo}/pulls?head={branch}&base=master&state=all'
    print(url)
    
    headers = {"Authorization": f"Bearer {token}"}
   
    response = requests.get(url, headers=headers)
    print("response:", response)

    if response.status_code != requests.codes.ok:
        return {}
    
    return response.json()


def is_exists_pr_for(owner, repo, branch, token, sha):
    all_prs = get_prs_for(owner, repo, branch, token)
    print("all_prs", all_prs)
    return any(map(lambda x: x["head"]["sha"] == sha, all_prs))
    


def create_pr_if_not_exists(owner, repo, branch, sha, message, token):
    if not is_exists_pr_for(owner, repo, branch, token, sha):
        print("Creating pr")
        return create_pr(owner, repo, branch, message, token)
    
    print("PR already exists")
    
    

def create_pr(owner, repo, branch, message, token):
    url = f'{GITHUB_API}/repos/{owner}/{repo}/pulls'
    print(url)

    title, body = message.split("\n")[0], "\n".join(message.split("\n")[1:])
    
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "title": title,
        "body": body,
        "head": branch,
        "base": "master",
    }
    print(f"data: {data}")
   
    response = requests.post(url, headers=headers, json=data)
    print("response:", response)

    if response.status_code != requests.codes.ok:
        return {}
    
    return response.json()
