# LN App Starter Code

This is a template that can be used to build LN Apps using the ZEBEDEE.io API.

Start by:
1. Set your secrets in replit OR create an .env file as shown below.


Example secrets or Template for .env (create in the ln_app directory with manage.py)
```
ZEBEDEE_API_KEY="API_KEY_GOES_HERE"
SECRET_KEY="YOUR_SECRET_KEY_HERE"
```

Example secrets or .env after complete setup. DON'T USE!
```
ZEBEDEE_API_KEY="xVEhDAbL648Wn55Airkm2vPdq8dD6haf"
SECRET_KEY="l@j7(nh13ctkn2)i)o=b#mycn1q%#6)23s#%b85x^z4-dd*6^)"
```

2. Installing the dependencies by navigating to the top-level ln_app directory and running pip install -r requirements.txt
3. Run the server by running python3 manage.py runserver in the same directory.


You can begin editing your project by navigating to zbd/views.py and begin writing your backend code. You can use the zbd/templates/zbd directory to add your templates to be rendered by the view.