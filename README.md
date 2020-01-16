# flask-dockerize-example-app
A simple dockerized flask app 

Setup
-----
1. Clone this repository.
2. Set `FLASK_ENV` environment variable as `development`, if you like to run flask in development mode.
3. Build docker container `docker-compose build`
4. Run the container `docker-compose up`  

Sample API requests
-------------------


##### Creating a request entity 

```bash
curl -X POST \
  http://localhost:5000/request/ \
  -H 'Content-Type: application/json' \
  -d '{
  "title": "witcher",
  "email": "test2@test.com"
}'
```
##### Retrieve a request entity by ID

```bash
curl -X GET http://localhost:5000/request/1/
```


##### Delete a request entity by ID

```bash
curl -X DELETE http://localhost:5000/request/1/
```
