# Getting Started

### Important things to note
- The docker container's base image has to be based on the x86 architecture, running an Apple Silicon native ARM container's base image will crash Elasticsearch server
- Running x86 image on Apple Silicon will run through a virtualization layer resulting in poor performance (~20mins for response) 
- After cloning the repository, add the MRTP pdf from the line mentioned below and place that file in the cloned directory. Name this file as ```MRTP.pdf```
```
https://drive.google.com/file/d/1tVriTSJmNwqwwS-N6ysqbEyRkxek34bz/view?usp=sharing
```

### Building the Docker container
- Run this command after cloning the repository (cd into the cloned repository first) 
```
docker build -t myapp .
```

- Elasticsearch uses port ```9200``` and ```9300```
- Flask server uses port ```6000```, this port can be changed from the env file

### Running the Docker container
- Use this command to run the container locally 
```
docker run --platform linux/x86_64 -p 9200:9200 -p 9300:9300 -p 6000:6000  myapp
```

