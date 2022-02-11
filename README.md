# four-bros-be

four-bros-be is the backend app for the four-bros-fe. The purpose of the backend is solely to return
the data necessary for the frontend to display.

Create a virtual environment to handle packages and dependencies
```
python3 -m venv four_bros
```

Activate your virtual environment
```
source four_bros/bin/activate
```

Install the necessary packages and modules
```
pip install -r requirements.txt
```

To add a new package/module to the virtual environment run the following command:
```
pip install <package>
```

If a new package was added to the virtual environment, run the following command to update the requirements.txt file:
```
pip freeze > requirements.txt
```


To run the app locally, use the following command from the app's home directory
```
python app.py
```

Happy coding!
