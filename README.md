# pyflask-mini
Minimalistic flask app in Docker  
This app give you  
"Success!" on /  
"Ok" on /ping  

### Build application
Build Docker image manually from git cloned repo 

```
$ git clone https://github.com/zopar/pyflask-mini.git
$ docker build -t zopar/pyflask-mini .
```

### Download precreated image
```
docker pull zopar/pyflask-mini
```

### Run the container
Create a container from image  

```
$ docker run --name pyflask-mini -d -p 8080:8080 zopar/pyflask-mini
```