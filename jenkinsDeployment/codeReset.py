import os
import sys

featureBranch = sys.argv[1]
targetBranch = sys.argv[2]
print("Need to push code from "+featureBranch+" to "+targetBranch+" Press enter Y confirm.")
userInp = input()
if(userInp.lower() == 'y'):
    print("Please wait")
    print (os.system('git checkout '+featureBranch))
    print (os.system('git pull origin '+featureBranch))
    print (os.system('git checkout '+targetBranch))
    print (os.system('git reset --hard '+targetBranch))
    print (os.system('git push origin --force '+targetBranch))
    print("Done.Thanks")
else:
    print("Thanks for wasting time")