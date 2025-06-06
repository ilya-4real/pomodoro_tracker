#! /usr/bin/env python

import argparse
from collections import namedtuple
import os
import time


def task_completed_notify(task_title: str) -> None:
    message = f"Great job! you have been working on task {task_title}. Now it is time to relax"
    os.system(f"notify-send '🍅 Pomodoro completed' '{message}'")
    print("🍅 Pomodoro completed", message)


Arguments = namedtuple("Arguments", ["minutes",  "task_title"])

def create_parser() -> Arguments:
    parser = argparse.ArgumentParser(
        "Pomodoro",
        "pomodoro 25 'task f521'",
        "Helps to track your time using Pomodoro 🍅",
    )
    parser.add_argument("minutes", help="for how long will timer run")
    parser.add_argument("task_title", help="What task you are working on")
    args = parser.parse_args()
    try:
        minutes = int(args.minutes)
        return Arguments(minutes, args.task_title)
    except ValueError:
        print("Invalid minutes value. It should be correct positive integer number. Using default 25 minutes")
    return Arguments(25, args.task_title)


def printProgressBar(
    iteration,
    total,
    prefix="",
    suffix="",
    decimals=1,
    length=100,
    fill="█",
    printEnd="\r",
):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + "-" * (length - filledLength)
    print(f"\r{prefix} |{bar}| {percent}% {suffix}", end=printEnd)
    # Print New Line on Complete
    if iteration == total:
        print()


def run_timer(minutes: int):
    ticks = 20
    wait_time = minutes / ticks * 60
    printProgressBar(0, 20, prefix="Progress:")
    for i in range(ticks):
        time.sleep(wait_time)
        printProgressBar(i, ticks, prefix="Progress:")

def show_current_pomodoro_info(minutes: int, task_title: str) -> None:
    print("🍅 New pomodoro session started.")
    print("🍅 Try to focus on your current task until the timer stops. Don't let others to interrupt you with talks or messages.")
    print("🍅 After the session end you can relax and do whatever you want")
    print(f"🍅 Your current task: '{task_title}'. Timer is set to run for {minutes} minutes")

def main():
    parser = create_parser()
    show_current_pomodoro_info(parser.minutes, parser.task_title)
    try:
        run_timer(parser.minutes)
        task_completed_notify(parser.task_title)
    except KeyboardInterrupt:
        print("\nThe pomodoro was stopped early. Try not to stop timer or lose focus")


if __name__ == "__main__":
    main()
