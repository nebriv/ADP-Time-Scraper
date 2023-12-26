# ADP-Time-Scraper

Probably only works on ADP V3?

## Setup and Configuration

1. Install requirements with `pip install -r requirements.txt`
2. Visit the ADP site to fetch your cookies and worker ID.
   2. Your worker ID (Shown below as $WORKERID) can be found in the URL GET requests.
	https://my.adp.com/myadp_prefix/time/v2/workers/$WORKERID/time-cards?$filter=timeCards/periodCode/codeValue eq 'current'&$expand=dayEntries
   3. View your request cookies after logging in and save them to cookies.json.
3. Copy settings.py.example to settings.py and add your worker id.
4. Run get_data.py to download your data
5. Run analysis.py to generate a simple graph