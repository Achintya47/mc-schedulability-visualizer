# README

## Purpose

This script provides a simple graphical interface to filter and visualize schedulability results for different real-time scheduling algorithms with respect to the Criticality Factor (CF).

It is intended as a lightweight utility to assist in exploratory analysis of experimental datasets.

---

## Requirements

* Python 3.8 or higher
* The following Python libraries:

  * pandas
  * matplotlib

> Note: `tkinter` is part of the standard Python distribution and typically does not require separate installation.

---

## Installation

It is recommended to use a virtual environment.

### Create and activate a virtual environment

**Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

**Linux / macOS:**

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Script

Ensure the dataset file is present in the same directory as the script.

```bash
python main.py
```

---

## Input Data

The script expects a CSV file with the following columns:

* Num_Tasks
* U_total
* HI_ratio
* CF
* Total_Generated
* EDF_VD_Schedulable_Count
* TT_Merge_Schedulable_Count
* IMC_PnG_Schedulable_Count
* EDF_IMC_Schedulable_Count

Column names must match exactly.

---

## Usage

* The interface presents dropdown menus for:

  * Num_Tasks
  * U_total
  * HI_ratio
  * CF

* Each dropdown includes a **"No Filter"** option.

* Selecting "No Filter" excludes that parameter from filtering.

After selecting the desired parameters, click **Plot** to generate the visualization.

---

## Notes

* If no records match the selected filters, no plot will be generated.
* Data is internally sorted by CF before plotting.
* The script is intended for small to moderate-sized datasets and interactive use.

---
