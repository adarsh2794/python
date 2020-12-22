import jenkins,os

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