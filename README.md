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

### Kubernetes deployment 
This deployment is based on nginx-ingress controller
We assume that you already have a cluster correctly setup and configured  
whit nginx-ingress controller
This deployment is tested on GKE

## Deploy app on kubernetes
```
kubectl apply -f deployment.yaml
```
Deployment.yaml contains, the Deployment part, Service and Nginx-ingress  
Warning: We use latest just becayuse this is an example. It is not for production use.

Wait a while and take the external ip
```
kubectl get ingress ingress-pyflask-mini
```

Point your browser on external ip, you will find Success! 
and on /ping you will find Ok


