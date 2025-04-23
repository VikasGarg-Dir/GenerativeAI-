# Chat with PDF's

## Introduction

---

Chat with PDF's is a Python application that helps you interact with pdf documents. You can upload PDF's of your liking and ask questions about the PDF's using natural language. The application will analyze the PDF content and provide you a relevent answer to your query.

## Dependencies & Installation

---

1: Clone the repository to your local machine

2: Install the following dependancies using
    
    `
	pip install -r requirements.txt
	`

3: Obtain an API Key from your OpenAI account and add it to the '.env' file present in the project directory. 

4: Add the PDF's you want to interact with in the 'files' folder present in the project directory.

## Usage

---

To run the application :

1: Download all the required dependencies and add the OpenAI API Key to the .env file

2: Run the 'ingest.py' to ingest the PDF's and create vectorembeddings from them.

3: Run the 'query_db.py' file to run the code.

