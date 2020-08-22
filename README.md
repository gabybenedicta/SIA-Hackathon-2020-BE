# Loungewie : Front-End
> React Native Mobile Application built for [Singapore Airlines AppChallenge 2020 - Singapore Student track](https://appchallenge.singaporeair.com/en/challenges/students)

This is the Back-End codebase for [Loungewie - A Mobile Queue Management System](https://github.com/maggiekoesno/SIA-Hackathon-2020/).

## Set Up
### Prerequisites
```
Python 3.6 or above
pip 20.1.1 or above
```
Make sure you have the `Python 3` and `pip` installed. You can verify your version by running:
```
python3 --version
pip3 --version
```

### Installation
#### Installing virtualenv
On macOs and Linux:
```
python3 -m pip install --user virtualenv
```
On Windows:
```
py -m pip install --user virtualenv
```
#### Creating a virtual environment
On macOS and Linux:
```
python3 -m venv env
```
On Windows:
```
py -m venv env
```
#### Activating a virtual environment
On macOS and Linux:
```
source env/bin/activate
```
On Windows:
```
.\env\Scripts\activate
```
#### Clone this repository
```
git clone https://github.com/gabybenedicta/SIA-Hackathon-2020-BE.git
```
#### Install requirements.txt
```
pip install -r requirements.txt
```
#### Migrate database
```
python manage.py migrate
```
#### Run server
```
python manage.py runserver
```

## Contributors
- Gabriella Benedicta Christianti
- Margaret Claire Koesno
- Stephanie Audrey Susanto
