PITCH-60-APP
Author
MACRINE ALICE ADHIAMBO "ALICIA"[https://github.com/Alicia-krynne]

Description
This is application aims to  mimic a blog. it is minimalist in nature. the App allows users to post blogs based on their interests. the user can sign in, post a blog, comment on other blogs and also like or dislike a blog.


LIVE PAGE




CLONNG THE  REPOSITORY:
https://github.com/Alicia-krynne/K-BLOG
Move to the folder and install requirements
cd pitch pitch-app
pip install -r requirements.txt (to  install dependecies)

Exporting Configurations
export SQLALCHEMY_DATABASE_URI=postgresql+psycopg2://{User Name}:{password}@localhost/{database name}
Running the application
python3 manage.py server
Testing the application
python3 manage.py test
Open the application on your browser 127.0.0.1:5000.

Technology used
1. Python :This is the main language in this project to create the methods and funtions needed. 
2. HTML: for creating the pages that are in the web app. also using HTML to manipulate the display. 
3. css : this is the styling language used for this app. Bootsrap is also added to make styling more efficient. 
4. shell&powershell : used to combine the flexibility of scripting, command-line speed, and the power of a GUI-based admin tool, in this case for our app.
5. Heroku :  for deploying the  app 

Known Bugs
The app can  fail to display  all blogs at  once but will show the blogs posted  by the user.

Contact Information
If you have any question or contributions, please email me at [alicakryne@outlook.com]

License
MIT License:
Copyright (c) 2021 Macrine Alice Adhiambo
