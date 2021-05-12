##Ping Service
Service that should send requests calls `ping`, it has port 5000 exposed. 

##Receiver Service 
Service that should send requests calls `receiver`, it has port 8080 exposed.

##Tests
`curl -X POST http://ping:5000/api/v1/ping -H "Content-Type: application/json" -d '{"url":"http://receiver:8080/api/v1/info"}'`