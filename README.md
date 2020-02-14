# ChatBot
This ChatBot is a basic program built in python and have the ability to interact with the user using programmed questions and responses.
Its ability is in understanding the inputs by looking for known patterns.
#Installation
1- Download the folder
2- Open it in a Shell command
3- Tap: 

1. Create VM instance
Check out the quickstart to create a Cloud Platform project and a Linux VM instance with Compute Engine, then SSH into it for the steps below. Pick a predefined machine type matching your preferred price and performance.

Container
Alternatively, you can use the Dockerfile to build a Docker container and run it on Compute Engine or other platforms.

docker build -t trump2cash .
docker tag trump2cash gcr.io/<YOUR_GCP_PROJECT_NAME>/trump2cash
docker push gcr.io/<YOUR_GCP_PROJECT_NAME>/trump2cash:latest
2. Set up auth
The authentication keys for the different APIs are read from shell environment variables. Each service has different steps to obtain them.

Twitter
Log in to your Twitter account and create a new application. Under the Keys and Access Tokens tab for your app you'll find the Consumer Key and Consumer Secret. Export both to environment variables:

export TWITTER_CONSUMER_KEY="<YOUR_CONSUMER_KEY>"
export TWITTER_CONSUMER_SECRET="<YOUR_CONSUMER_SECRET>"
If you want the tweets to come from the same account that owns the application, simply use the Access Token and Access Token Secret on the same page. If you want to tweet from a different account, follow the steps to obtain an access token. Then export both to environment variables:

export TWITTER_ACCESS_TOKEN="<YOUR_ACCESS_TOKEN>"
export TWITTER_ACCESS_TOKEN_SECRET="<YOUR_ACCESS_TOKEN_SECRET>"
Google
Follow the Google Application Default Credentials instructions to create, download, and export a service account key.

export GOOGLE_APPLICATION_CREDENTIALS="/path/to/credentials-file.json"
You also need to enable the Cloud Natural Language API for your Google Cloud Platform project.

TradeKing
Log in to your TradeKing account and create a new application. Behind the Details button for your application you'll find the Consumer Key, Consumer Secret, OAuth (Access) Token, and Oauth (Access) Token Secret. Export them all to environment variables:

export TRADEKING_CONSUMER_KEY="<YOUR_CONSUMER_KEY>"
export TRADEKING_CONSUMER_SECRET="<YOUR_CONSUMER_SECRET>"
export TRADEKING_ACCESS_TOKEN="<YOUR_ACCESS_TOKEN>"
export TRADEKING_ACCESS_TOKEN_SECRET="<YOUR_ACCESS_TOKEN_SECRET>"
Also export your TradeKing account number, which you'll find under My Accounts:

export TRADEKING_ACCOUNT_NUMBER="<YOUR_ACCOUNT_NUMBER>"
3. Install dependencies
There are a few library dependencies, which you can install using pip:

$ pip install -r requirements.txt
4. Run the tests
Verify that everything is working as intended by running the tests with pytest using this command:

$ export USE_REAL_MONEY=NO && pytest *.py -vv
5. Run the benchmark
The benchmark report shows how the current implementation of the analysis and trading algorithms would have performed against historical data. You can run it again to benchmark any changes you may have made:

$ python benchmark.py > benchmark.md
