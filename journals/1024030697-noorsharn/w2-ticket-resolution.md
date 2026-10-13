# Week 2: Structuring the 60-Day Student Behavioral Dataset

## Ticket Summary
**ID:** `DATA-002`  
**Assignee:** Noorsharn Singh (Frontend UI/UX Engineer & Data Modeling Specialist)  
**Date:** August 23, 2026  
**Status:** Closed / Resolved  

---

## Problem / Error Description
Testing memory ingestion and decision simulation required a realistic, longitudinal behavioral dataset. Relying on superficial dummy data (such as three generic sentences) made it impossible to evaluate whether the twin could detect circadian energy dips, class commitments, or travel constraints.

---

## Relevant Context
A student's daily routine involves fixed constraints (college lectures, lab sessions, transit) interspersed with discretionary blocks (project work, gaming, study sessions). To train and benchmark Alter, we needed continuous time-series data reflecting real daily pressures.

---

## Key Observation & Root Cause Analysis
For behavioral modeling, each dataset record needs to capture both objective parameters (start time, end time, duration, fixed vs discretionary) and subjective state variables (energy level from 1–5, distraction level, task completion status).

---

## Solution
Engineered and validated the 60-day behavioral dataset in `dataset/continuous_60_day_ai_schedule_dataset.csv`:

```csv
date,day_of_week,time_start,time_end,duration_min,activity,category,is_fixed_schedule,class_hours,travel_minutes_today,academic_workload_before_slot_min,energy_level_1_5,distraction_level,priority,continuous_free_time_min,can_complete_task,best_time_for_task,task_completed
2026-09-01,Tuesday,06:30,07:15,45,Morning Routine + Breakfast,Routine,1,3.0,145,228,,,,45,,,
2026-09-01,Tuesday,07:15,09:00,105,Travel / Free Time,Travel,1,3.0,145,228,,,,105,,,
2026-09-01,Tuesday,09:00,12:00,180,College Classes,Academic,1,3.0,145,228,,,,180,,,
2026-09-01,Tuesday,12:00,12:40,40,Travel / Commute,Travel,1,3.0,145,228,,,,40,,,
2026-09-01,Tuesday,14:15,16:36,141,Project Work,Academic,0,3.0,145,228,4,Medium,Medium,141,1,14:15,0
2026-09-01,Tuesday,19:24,20:51,87,DBMS Study,Academic,0,3.0,145,228,5,Low,Medium,87,1,19:24,1
```

Over 660 sequential time blocks were generated, capturing realistic variations across weekdays and weekends.

---

## Because
High-granularity behavioral data provides grounded evidence for semantic rule extraction (e.g., detecting fixed class obligations) and behavioral correlation (e.g., assessing task completion drop-offs under high distraction).
