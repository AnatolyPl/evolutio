# Evolutio

# Start service
Clone repository and type cmd command "docker-compose up --build" in the root directory of the project.  
  
Guide for installing docker - https://docs.docker.com/get-started/

# Visit API documentation page
Visit http://localhost:8001/api/docs for OpenAPIv3 documentation.  
Here you can try out both of endpoints.  
Sample dataset already in the database.  
Second endpoint param is a little bit tricky due to specification standarts.  
Just type param in json format {"reference":"1489"} or {"id": "1"}  

# Admin page
To modify or browse data (http://localhost:8001/admin) use credentials:  
  login: evolutio  
  password: evolutio_test
