import os
import sys
import jenkins



def deployJob():
    print(os.system("pip install python-jenkins"))
    try:
        print("Enter username")
        inUser = input()
        print("Enter password")
        inpPass = input()
        server = jenkins.Jenkins('http://10.10.20.206:8080', username=inUser, password=inpPass)
        user = server.get_whoami()
        version = server.get_version()
        jobs = server.get_jobs()
        print('Hello %s from Jenkins %s' % (user['fullName'], version))
        jobMap = {}
        print('Jobs are ')
        for i in range(len(jobs)):
            jobMap[i] = jobs[i].get('fullname')
            print(str(i)+". "+jobMap[i])

        print("Enter the job number to deploy")
        jobNum = input()
        print("Job to deploy "+jobMap[int(jobNum)]+" Press Y to cofirm build trigger")
        server.build_job(jobMap[int(jobNum)])
    except:
        print("Some error occured")



featureBranch = sys.argv[1]
targetBranch = sys.argv[2]
print("Need to push code from "+featureBranch+" to "+targetBranch+" Press enter Y confirm.")
userInp = input()
if(userInp.lower() == 'y'):
    print("Please wait")
    print (os.system('git checkout '+featureBranch))
    print (os.system('git pull origin '+featureBranch))
    print (os.system('git checkout '+targetBranch))
    print (os.system('git reset --hard '+featureBranch))
    print (os.system('git push origin --force '+targetBranch))
    print("Done.Thanks")
    print("Do you want to deploy "+targetBranch+" Press enter Y confirm.")
    userInp = input()
    if(userInp.lower() == 'y'):
        deployJob()
else:
    print("Thanks for wasting time")