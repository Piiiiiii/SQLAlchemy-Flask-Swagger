# Database for Flask App

## Run with virtualenv
- Create a virtualenv folder `virtualenv -p python3 venv`
- Activate `source venv/bin/activate`
- Install the requirements `pip install -r requirements.txt`
- Run gunicorn `gunicorn app:app --bind 0.0.0.0:5000 --reload`

## Run with Docker
- Build the image with `sudo docker build -t hello-app .`
- Run the container with `sudo docker run -d -p 5000:5000 -e PORT=5000 --name hello-server hello-app`
- Check that the container is running
- Go to `localhost:5000`. You should see `Hello, World!`

## Update for psycopg2
- New requirement psycopg2-binary==2.8.4
- Users can connect to psycopg2 and create a new table

## Update APIs
- Update apis of user, campaign, topic, article and tag
- Build tables

## Update APIDocs and error message
