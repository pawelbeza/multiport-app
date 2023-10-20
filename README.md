multiport-webserver
=========
multiport webserver is a simple app which launches webserver for each specified port 
(you can specify as many ports as you want)

```
python3 multiport-webserver --port 8080 8081
```
OR
```
docker run -p 8080:8080 -p 8081:8081 pbeza/multiport-app:latest -p 8080 8081
```

Then visit http://localhost:8080/ or http://localhost:8081/ in your browser.