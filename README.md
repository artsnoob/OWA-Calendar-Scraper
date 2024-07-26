# OWA Calendar Scraper

This Python script automates the process of scraping calendar events from Outlook Web App (OWA) using Selenium WebDriver. It's designed to navigate to your OWA calendar, interact with the weekly view, and extract event details for the current week.

## Features

- Automated login to OWA (requires manual user intervention)
- Navigation to the weekly calendar view
- Interaction with the calendar to reveal all events
- Scraping of event details including title, date, and time
- Saving extracted events to a text file

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.6 or higher
- pip (Python package manager)
- Google Chrome browser installed

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/owa-calendar-scraper.git
   cd owa-calendar-scraper
   ```

2. Install the required Python packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the script:
   ```
   python owa_calendar_scraper.py
   ```

2. When prompted, manually log in to your OWA account and navigate to the weekly calendar view.

3. Press Enter in the console to continue the script execution.

4. The script will interact with the calendar and attempt to scrape the events.

5. If successful, the events will be displayed in the console and saved to a file named `calendar_events_current_week.txt`.

## Troubleshooting

If the script fails to scrape events:

1. Ensure you're logged in and can see events in the weekly view before continuing the script.
2. Check that your OWA interface matches the expected structure. You may need to adjust the CSS selectors in the script.
3. Look for any error messages in the console output for clues about what might be going wrong.
