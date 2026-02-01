# Steam Review Reducer
[![Ask DeepWiki](https://devin.ai/assets/askdeepwiki.png)](https://deepwiki.com/dragon99z/Steam-Review-Reducer)

A Python script that fetches all reviews for a given Steam AppID and recalculates the review score by filtering out reviews from users with less than a specified minimum playtime. This allows you to see how the rating changes when you only consider players who have spent a certain amount of time in the game.

## Features

-   Fetches all public reviews for any game on Steam.
-   Calculates the original positive review percentage.
-   Prompts the user to enter one or more minimum playtime thresholds (in minutes).
-   Recalculates the review score for each specified threshold, ignoring reviews below it.
-   Displays a clear comparison between the original and filtered review scores.
-   Handles Steam API pagination to retrieve all reviews, regardless of the total count.

## Prerequisites

-   Python 3
-   The `requests` library

## Installation

1.  Clone the repository to your local machine:
    ```sh
    git clone https://github.com/dragon99z/Steam-Review-Reducer.git
    cd Steam-Review-Reducer
    ```

2.  Install the required Python packages using pip:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1.  Run the script from your terminal:
    ```sh
    python steam_appreviews_sum.py
    ```

2.  When prompted, enter the Steam AppID for the game you want to analyze. You can find the AppID in the game's store page URL (e.g., `https://store.steampowered.com/app/570/` for Dota 2, where `570` is the AppID).

3.  Next, enter the minimum playtime in minutes. You can enter a single number or a comma-separated list of numbers to check multiple thresholds at once.

### Example

Here is an example of running the script for a fictional game with AppID `12345`:

```
$ python steam_appreviews_sum.py
Enter the steam appid you want to check: 12345
Fatching all reviews
0.0% done.
14.29% done.
...
100.0% done.

---------------------------------------------------------------

Enter the minimum amount of minuts
a review should have (can spereated by ,): 60,300

---------------------------------------------------------------

Cehcking for AppID: 12345 and minimum minuts of 60

Total Votes: 750
Total Up Votes: 600
Total Down Votes: 150
Total Rating Ratio: 80.0

Reduced Up Votes: 550
Reduced Down Votes: 50
Reduced Rating Ratio: 91.67

---------------------------------------------------------------

Cehcking for AppID: 12345 and minimum minuts of 300

Total Votes: 750
Total Up Votes: 600
Total Down Votes: 150
Total Rating Ratio: 80.0

Reduced Up Votes: 400
Reduced Down Votes: 25
Reduced Rating Ratio: 94.12

---------------------------------------------------------------