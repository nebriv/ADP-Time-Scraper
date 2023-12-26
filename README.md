# ADP-Time-Scraper

Requests time off data from ADP via their frontend API. Downloads the vacation and sick time data to a json file. Probably only works on ADP V3?

Example output

<img width="708" alt="image" src="https://github.com/nebriv/ADP-Time-Scraper/assets/1825214/82a4a7e3-3417-4dab-b372-334bf81bc5ea">

## Setup and Configuration

1. Install requirements with `pip install -r requirements.txt`
2. Visit the ADP site to fetch your cookies and worker ID.

   1. Your worker ID (Shown below as $WORKERID) can be found in the URL GET requests (view the network requests.
	https://my.adp.com/myadp_prefix/time/v2/workers/$WORKERID/time-cards?$filter=timeCards/periodCode/codeValue eq 'current'&$expand=dayEntries

   2. View your request cookies after logging in and save them to cookies.json.
4. Copy settings.py.example to settings.py and add your worker id.
5. Run get_data.py to download your data
6. Run analysis.py to generate a simple graph
