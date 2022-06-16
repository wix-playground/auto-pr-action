import os
from github_adapter import get_commit, create_pr

def should_create_pr(message):
    auto_pr_hashtags = {
        "#test_auto_pr",
        # "#pr",
        # "#automerge"
    }
    for hashtag in auto_pr_hashtags:
        if hashtag in message:
            return True
    return False


def main():
    commit_sha = os.getenv("GITHUB_SHA")
    token = os.getenv("INPUT_GITHUB_TOKEN")
    owner, repo = os.getenv("GITHUB_REPOSITORY").split("/")
    branch = os.getenv("GITHUB_REF_NAME")
    
    print(f'commit_sha {commit_sha}')
    print(f'owner {owner}')
    print(f'repo {repo}')
    print(f'branch {branch}')
    print(f'token {token}')
    
    commit = get_commit(owner, repo, commit_sha, token)
    commit_message = commit["commit"]['message']

    if should_create_pr(commit_message.lower()):
        create_pr(owner, repo, branch, commit_message, token)

if __name__ == "__main__":
    main()