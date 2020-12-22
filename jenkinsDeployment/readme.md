Hey Guys,Sharing 2 python scripts I wrote which will help in 
1.Pushing code from the feature branch to the dev branch 
2.Deploy the Jenkins job from the list of jobs
How to Use1.Make Sure Python 3 or above is installed in your system2.Make Sure the file Path given by you is correct and you are currently inside a git repo
Terminal Command 1.To push code as well as deploy
python ../codeResetAndDeploy.py <feature-branch> <deployment-branch>Eg:python ../codeResetAndDeploy.py sprint-8 dev-3
(Provided file is kept at one level before all the projects folder)
2.To Deploy any Jobpython ../DeployJenkins.py




