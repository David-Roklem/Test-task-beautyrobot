# Test-task-beautyrobot

## Task 1
This task is made in two variants depending on the task specification interpetation. Just in case :)

Run task_1/verify_input_data.py

## Task 2
Run task_2/count_elements.py

## Task 4
For checking this task a MongoDB client is required in your system. Probably, it's easier to use Docker (as I did). You'll need the following commands to upload and run MongoDB client in Docker container:
```
docker pull mongo:latest
docker run -d -p 2717:27017 --name mongo_container mongo:latest
docker exec -it mongo_container mongosh
```
Now you're inside mongo_container and can create task_db:
```
> use task_db
```
Now you can run mongo.py from task_4/mongo.py

## Task 5
This webhook example is based on FastAPI framework. This task implementation requires to use some service that will help to expose localhost to the internet (rather than deploying the project). I chose to use [Pinggy](https://pinggy.io/). First of all, you'll need to sign up there and then copy and paste the command from Pinggy main page to you terminal in order to get an URL exposed to the internet:

![Pinggy main page](https://github.com/David-Roklem/Test-task-beautyrobot/blob/main/Pinggy-main-page.png)

After pasting and running the command from Pinggy in your terminal you'll get something like this:

![Pinggy in terminal](https://github.com/David-Roklem/Test-task-beautyrobot/blob/main/Pinggy_terminal.png)

Next step is to copy any of the URLs provided by Pinggy from your terminal and use it as POST request address. In my case I user Postman (desktop version of it - web version will not work with localhost!). You can use other tools, curl, for example.

Then run uvicorn server (The entrypoint of Task 5 is webhook_handler.py - just run it) and it's ready to accept requests:

![Webhook example using Pinggy and Postman](https://github.com/David-Roklem/Test-task-beautyrobot/blob/main/POSTMAN_WEBHOOK.gif)
