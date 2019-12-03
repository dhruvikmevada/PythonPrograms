from git import Repo
path = Repo('./')
# print(path.active_branch.name)

if path.active_branch.name == 'master':
    print("This is a master branch")
else:
    print("This is not a master branch")