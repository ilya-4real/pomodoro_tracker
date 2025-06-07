# Pomodoro tracker created for personal usage

### 1. Installation
clone the repo:
~~~bash
git clone https://github.com/ilya-4real/pomodoro_tracker.git
# make main.py file executable
chmod +x main.py

# create soft link or clone the file to ~/.local/bin
cp main.py ~/.local/bin/pomodoro
~~~

### 2. Initialize tasks storage

~~~bash
pomodoro init
~~~

### 3. Run the tracker 

Just run command `pomodoro` with 2 arguments:
- minutes: time to run the timer
- task_title: current task you are working on

Example:
~~~bash
pomodoro focus 30 "Task 225 from jira"
~~~


### 4. Get help

~~~bash
pomodoro --help
~~~
