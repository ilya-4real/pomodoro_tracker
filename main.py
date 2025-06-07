#! /usr/bin/env python

import argparse
import os
import time

from internal.database import AppConfig, SqliteTaskDatabase, Task


def task_completed_notify(task_title: str) -> None:
    message = f"Great job! you have been working on task {task_title}. Now it is time to relax"
    os.system(f"notify-send '🍅 Pomodoro completed' '{message}'")
    print("🍅 Pomodoro completed", message)


def create_parser():
    parser = argparse.ArgumentParser(
        "Pomodoro",
        "pomodoro focus 25 'task f521'",
        "Helps to track your time using Pomodoro 🍅",
    )
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    subparsers.add_parser("init", help="Initialize local tasks database")

    focus_parser = subparsers.add_parser("focus", help="Start new 🍅 Pomodoro session")
    focus_parser.add_argument("minutes", type=int, help="for how long will timer run")
    focus_parser.add_argument("task_title", help="What task you are working on")

    subparsers.add_parser(
        "report", help="Create csv file with all 🍅 Pomodoro sessions"
    )

    return parser.parse_args()


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
    print(
        "🍅 Try to focus on your current task until the timer stops. Don't let others to interrupt you with talks or messages."
    )
    print("🍅 After the session end you can relax and do whatever you want")
    print(
        f"🍅 Your current task: '{task_title}'. Timer is set to run for {minutes} minutes"
    )


def run_task(run_minutes: int, task_title: str):
    start_timestamp = round(time.time())
    show_current_pomodoro_info(run_minutes, task_title)
    try:
        run_timer(run_minutes)
        task = Task(task_title, start_timestamp, round(time.time()), True)
        task_completed_notify(task_title)
    except KeyboardInterrupt:
        task = Task(task_title, start_timestamp, round(time.time()), False)
        print(
            "\nThe pomodoro was stopped early and it is marked as unfinished. Try not to stop timer or lose focus"
        )
    return task


def evaluate_command(config: AppConfig, args: argparse.Namespace):
    match args.command:
        case "init":
            print(f"Pomodoro is initialized and tasks will be stored in {config.file_path}")
            SqliteTaskDatabase.init_database(config)
        case "focus":
            task = run_task(args.minutes, args.task_title)
            database = SqliteTaskDatabase(config)
            database.insert_task(task)

        case "report":
            print("Generating csv file with all activities...")


def main():
    args = create_parser()
    evaluate_command(AppConfig(), args)

if __name__ == "__main__":
    main()
