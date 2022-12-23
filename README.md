# to do lists in telegram!

hey, this is my test project to learn how to make telegram-bots.
<br><br><br>

## how to run

1) install python, pip, git (if you don't have it)
2) clone this repo
3) install virtualenv and use it in project folder
4) install requirements
5) run bot using *python3 setup.py*

### envs

Open .env.example, set up your environment variables and rename file to .env <br>

Insert your token from BotFather in TOKEN line. <br>
Other variables you should know (with your database). <br>

If you use docker with postgres, you might have problems with HOST variable. Try the following command in your terminal:

**docker inspect --format='{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' some-postgres**

This will give you the IP address of the container. <br>

### database

in process..... 
<br><br><br>

## next steps

- [ ] add location support
- [ ] add tests
- [ ] write additional information (some help pages like resources, database setup instructions, problem solving and so on)