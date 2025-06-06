# Pomodoro tracker created for personal usage

### 1. Installation
clone the repo:
~~~bash
git clone https://github.com/ilya-4real/pomodoro_tracker.git
# make pomodoro file executable
chmod +x pomodoro

# create soft link or clone the file to ~/.local/bin
cp main.py ~/.local/bin/pomodoro
~~~


### 2. Run the tracker 

Just run command `pomodoro` with 2 arguments:
- minutes: time to run the timer
- task_title: current task you are working on

Example:
~~~bash
pomodoro 30 "Task 225 from jira"
~~~


### 3. Get help

~~~bash
pomodoro --help
~~~
