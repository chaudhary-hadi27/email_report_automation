# Email Report Automation Script

## Overview

This Python script automates the process of handling weekly email reports. It downloads CSV attachments from unread emails with the subject "Report", cleans and standardizes the data, merges multiple files into a single weekly report, generates summary statistics, and saves the results with timestamps for easy tracking.

## Features

* Automatically connects to Gmail and retrieves unread emails with a specific subject.
* Downloads CSV attachments.
* Cleans data by removing extra spaces and standardizing text formatting.
* Merges multiple CSV files into one comprehensive weekly report.
* Generates summary statistics for numeric columns.
* Saves reports and summaries with timestamps in designated folders.

## Requirements

* Python 3.x
* pandas

Install dependencies with:

```
pip install pandas
```

## Usage

1. Clone or download the repository.
2. Update the configuration section in `email_report_automation.py` with your Gmail credentials and preferred folder paths.
3. Run the script:

```
python email_report_automation.py
```

4. Check the processed and summary folders for cleaned CSVs, merged weekly report, and summary statistics.

## Folder Structure

* `downloads/` : Stores downloaded CSV attachments.
* `processed/` : Stores cleaned and formatted CSV files.
* `summary/` : Stores the final weekly report and summary statistics.

## Security Note

* Avoid committing your Gmail credentials to a public repository.
* Consider using environment variables or a configuration file to securely manage sensitive data.

## Future Enhancements

* Schedule the script to run automatically using cron (Linux/macOS) or Task Scheduler (Windows).
* Add email notifications after the weekly report is generated.

## License
This project is licensed under the MIT License.
LICENSE
