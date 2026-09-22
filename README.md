# Welcome to **SpendManager**
An open source financial manager and tracker, totally free. No adds. No payments


# Whats makes SM different to another apps, softwares, spreadsheets or paper?
* The app works in your computer without external servers.
* It's totally private and secure.
* You can see the all the code use for the app.
* It runs in your browser by Streamlit.
* You can add or delate anything you want.
* No vibecode used.

# How it works?
It works in three diferent Python files ,that we'll show later, and a database. It use Streamlit so it can be self-hosted and easy editable.

*You can see what library requieres in requirements.txt*

# Files and recommended use.

We recommend to know how to write simply code with Python using Pandas, Streamlit and some SQL to talk to the database.
Or you can use AI.

**The Files**

**APP.py:** This file is the one in charge of the app, uses the function in the other files and shows in Streamlit. It's the main file.

**NP.py:** Only uses NumPy.

**SQL.py:** As it name say's, this uses SQL to call the database. Please be very carefull if you edit this.

**database.db:** Here all your data it,s saved. If you want to see the data inside you must use an SQL viewer, we recommend *SQLite viewer* from *Florian Klampfer* in VS Code, also the *SQLite* extension from *alexcvzz*

# To run the app you need to use the foward command:

*Stramlit run ""
