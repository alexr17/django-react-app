# DealDock Main Site

Clone this repository (into your work folder) and cd into it:
```
git clone https://github.com/alexr17/dealdock
cd dealdock
```

## Frontend

## Backend

All of the configuration and setup should go here.

### Environment Setup

#### External Things
When setting up your environment you will need to install a few things separately: `python3`, `venv` (this stands for `virtualenv` but you can use some other python environment manager), and `pip3`. However you go about installing these really depends on your machine and OS. For example if you have a Mac you can use homebrew to install all of these.

#### Generating Environment
Once you have these packages installed you should be able to access python3 through the terminal executable `python3`. You should also be able to run `pip3` or `pip`.

To generate your local environment use the following steps (make sure you are in the top-level directory of this project `~/../dealdock`)
```
python3 -m venv backend
cd backend
source bin/activate
pip3 install -r requirements.txt
```

If you use vscode, add this to your `settings.json`:
```
"python.pythonPath": "backend/bin/python"
```

#### Adding Packages
When installing packages make sure you are in `dealdock/backend`, not `dealdock`. Install your package like so:
```
pip3 install <your package here>==<optional version #>
pip3 freeze > requirements.txt
```
Everytime you add packages to the requirements.txt, let everyone know so they can install the new package(s).