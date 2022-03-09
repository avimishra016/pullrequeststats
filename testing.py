import yaml
from github import Github

repos = ""
accessToken = ""
with open(r'C:/Users/aweso/Downloads/Visual Studio Coding/python/repo.yaml') as file:
    documents = yaml.full_load(file)
    repos = documents['repos'][0]
    accessToken = documents['accessToken'][0]

print(repos)
print(accessToken)
g = Github(accessToken)
for repo in g.get_user().get_repos():
    print(repo.name)
    if (repo.name=='pullrequeststats'):
        pulls = repo.get_pulls(state='open', sort='created', base='main')
        print("Number, title, date opened, last comment date, reviewers, num approved, num pending")
        for pr in pulls:
            print(pr.number, ", ", pr.title, ", ", pr.created_at)
