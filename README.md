[![Build Status](https://travis-ci.com/alexr17/dealdock.svg?token=eTSsnFCxpGUesGuyt7Xm&branch=master)](https://travis-ci.com/alexr17/dealdock)

# DealDock Main Site

Clone this repository (into your work folder) and cd into it:
```
git clone https://github.com/alexr17/dealdock
cd dealdock
```

## Deployment

### Setting up environment

Install the Heroku CLI: https://devcenter.heroku.com/articles/heroku-cli. Once installed you should be able to use the `heroku` command. At this point you will need to copy the following information into a file. The reason for this is that I do not want each of you logging into my heroku account on your own CLI. Paste this information into `dealdock/.git/config`:

```
[remote "heroku"]
	url = git@heroku.com:dealdock.git
	fetch = +refs/heads/*:refs/remotes/heroku/*
```

Now when you run the command `git remote -v`, you should see a heroku remote pop up in addition to the github one.

### SSH Stuff

Rather than have you all login to my account to deploy the app, everyone will create their own ssh keys that they send to me. If you don't know about ssh you should google some. To generate an ssh key, navigate to `~/.ssh` (or create it if you don't have it) and run the command `ssh-keygen -t rsa`. Send me the resulting `.pub` file. I will paste it into heroku so they can recognize you when you deploy.

### Deploying

Once I have put the ssh key into heroku, you should be able to deploy the app from your local by running the following command:
```
git push heroku master
```
!!! Warning !!! This initiates a deployment process which cannot be undone by ^C. If you need to undo a deployment, simply push again with new commits and a new build will be generated. That being said, we are rate-limited to 75 heroku git requests an hour, so please don't hammer the deployment process.

## Frontend

### Building
```
npm run build
```

### Running Frontend (in development)
```
npm start
```

## Backend

### Running Backend (in development)

The basic command to run the backend in development is:
```
python manage.py runserver
```

### Environment Setup

#### External Things
When setting up your environment you will need to install a few things separately: `python3`, `venv` (this stands for `virtualenv` but you can use some other python environment manager), and `pip3`. However you go about installing these really depends on your machine and OS. For example if you have a Mac you can use homebrew to install all of these.

#### Generating Environment
Once you have these packages installed you should be able to access python3 through the terminal executable `python3`. You should also be able to run `pip3` or `pip`.

To generate your local environment use the following steps (make sure you are out of the top-level directory)
```
python3 -m venv dealdock
cd dealdock
source bin/activate
pip3 install -r requirements.txt
```

If you use vscode, add this to your `settings.json`:
```
"python.pythonPath": "bin/python"
```

#### Adding Packages
Install your package like so:
```
pip3 install <your package here>==<optional version #>
pip3 freeze > requirements.txt
```
Everytime you add packages to the requirements.txt, let everyone know so they can install the new package(s).