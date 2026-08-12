# CAP 776 — Daily Activity Tracker

## My Data, My Code

This repository contains my **Daily Activity Tracker dataset** for **CAP 776 — Python Programming**.

The dataset is maintained in a single Excel (`.xlsx`) file named using my registration number. Each row in the **Daily Log** sheet represents one day and records how I spent my time, along with basic information about my daily feeling, satisfaction, energy level, and notes.

## Repository Contents

* `<RegistrationNumber>.xlsx` — Main daily activity dataset.

## Dataset Structure

The Excel workbook contains two sheets:

### 1. Instructions

The first sheet contains instructions for maintaining the dataset, including:

* File naming requirements
* Where to enter daily data
* Time-format guidelines
* Column descriptions
* Good practices for maintaining consistent records

### 2. Daily Log

The **Daily Log** sheet contains one row for each day.

| Column                 | Description                                                  |
| ---------------------- | ------------------------------------------------------------ |
| Date                   | Calendar date of the entry                                   |
| Sleep (min)            | Total sleep duration in minutes                              |
| Fitness (min)          | Workout, sports, walking, yoga, etc.                         |
| Study (min)            | Academic study or reading time, excluding coding             |
| Coding (min)           | Programming, lab, or project work                            |
| Class (min)            | Time spent in scheduled lectures/labs                        |
| Classes Attended       | Number of class sessions attended                            |
| Other Activities (min) | Chores, social activities, hobbies, and other activities     |
| Total Tracked (min)    | Automatically calculated total of tracked time               |
| Free/Unaccounted (min) | Automatically calculated remaining time out of 1,440 minutes |
| Day's Feeling          | Daily feeling selected from the available options            |
| Satisfaction Level     | Daily satisfaction level                                     |
| Energy Level           | Daily energy level                                           |
| Notes                  | Short description explaining the day or anything unusual     |

## Time Format

All activity durations are recorded **in minutes**.

For example:

* 2.5 hours of study → `150` minutes
* 45 minutes of fitness → `45` minutes
* 8 hours of sleep → `480` minutes

Using a single unit makes the dataset easier to process and analyze with Python.

## Dataset Purpose

The dataset is maintained as part of **CAP 776 — Python Programming** and can be used for practicing Python-based:

* Data loading and cleaning
* Excel file handling
* Data analysis
* Statistical summaries
* Visualization
* Time and activity pattern analysis

The dataset will be updated regularly as new daily activity records are added.

## Data Entry Guidelines

* Add one row for each day.
* Record all durations in minutes.
* Keep the automatically calculated cells unchanged.
* Use the provided dropdown options for feeling, satisfaction, and energy.
* Add short notes when something unusual affects the day's routine.
* Maintain the dataset consistently over time.


## Course

**Course:** CAP 776 — Python Programming
**Dataset:** Daily Activity Tracker
**Format:** Excel (`.xlsx`)

> This repository is maintained for academic and course-related purposes.
