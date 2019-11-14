[![Build Status](https://travis-ci.com/alexr17/dealdock.svg?token=eTSsnFCxpGUesGuyt7Xm&branch=master)](https://travis-ci.com/alexr17/dealdock)

# DealDock Main Site

Clone this repository (into your work folder) and cd into it:
```
git clone https://github.com/alexr17/dealdock
cd dealdock
```

The information in this README covers setting up your actual codebase in your development environment. For database, deployment, and other setup, please navigate here: https://www.notion.so/dealdock/Engineering-Onboarding-380a88d2e14441398667ad69bd3747ce

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

To test backend run
```
python manage.py test
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