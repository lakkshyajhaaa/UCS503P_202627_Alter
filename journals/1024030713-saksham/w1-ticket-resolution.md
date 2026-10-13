# Week 1: Git Branching & Multi-OS Line-Ending Normalization

## Ticket Summary
**ID:** `INFRA-001`  
**Assignee:** Saksham Raj (Full-Stack & Cloud Infrastructure Engineer)  
**Date:** August 15, 2026  
**Status:** Closed / Resolved  

---

## Problem / Error Description
During the initial repository setup across team workstations running Windows and Linux, Git reported false modifications across the entire source tree upon cloning. Running `git status` displayed dozens of clean files as unstaged modifications with repeated warnings:

```
warning: LF will be replaced by CRLF in Makefile.
The file will have its original line endings in your working directory.
```

Unchecked commits from different operating systems also risked injecting carriage returns (`\r\n`) into shell scripts and Python virtual environments, breaking POSIX test runners.

---

## Relevant Context
In multi-platform engineering teams, Windows environments use Carriage Return + Line Feed (`CRLF`), whereas Linux and macOS use Line Feed (`LF`). Without repository-level enforcement, Git automates conversions inconsistently, causing noisy diffs and breaking automated linting pipelines.

---

## Key Observation & Root Cause Analysis
The repository lacked a top-level `.gitattributes` file. Git's core `autocrlf` setting on individual workstations differed, causing file hashes to diverge on checkout even when the actual text content was identical.

---

## Solution
1. **Created Repository-Wide `.gitattributes`:**
   ```gitattributes
   # Enforce LF endings across all text files
   * text=auto eol=lf

   # Explicit OS-specific script handling
   *.bat text eol=crlf
   *.ps1 text eol=crlf
   *.sh text eol=lf

   # Mark binary files to prevent corruption
   *.sqlite binary
   *.png binary
   *.jpg binary
   *.pdf binary
   ```
2. **Renormalized Git Index:**
   ```bash
   git add --renormalize .
   git commit -m "chore: normalize line endings via .gitattributes"
   ```
3. Configured feature branching guidelines to ensure `master` remains stable for cloud staging deploys.

---

## Because
Establishing centralized line-ending rules in `.gitattributes` prevents corrupt binary checkouts, guarantees that shell scripts and Makefiles run reliably across both Linux and Windows, and eliminates noisy git diffs.
