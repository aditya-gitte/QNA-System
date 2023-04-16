FROM --platform=linux/x86_64 python:3.9-slim-buster


#install the python dependencies
RUN pip install --upgrade pip
RUN pip install Flask
RUN pip install --upgrade pip setuptools wheel
RUN pip install Flask-Cors==3.0.10 


#fixing shap
RUN apt-get update && \
    apt-get install -y gcc g++ make cmake
RUN pip install numpy pandas scipy scikit-learn matplotlib
RUN pip install shap

RUN pip install farm-haystack[ocr]
RUN yes | apt-get install poppler-utils


# Install, update permissions and run Elasticsearch
RUN apt-get update
RUN apt-get install -y wget
RUN wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-7.9.2-linux-x86_64.tar.gz -q 
RUN tar -xzf elasticsearch-7.9.2-linux-x86_64.tar.gz 
# RUN chown -R elasticsearch:elasticsearch elasticsearch-7.9.2
# RUN chown -R daemon:daemon elasticsearch-7.9.2
RUN chmod -R 777 elasticsearch-7.9.2 

RUN apt-get update && apt-get install -y netcat
RUN apt install curl
RUN pip install python-dotenv


WORKDIR /app
COPY . /app
RUN mkdir /app/Documents
RUN chmod +x runner.sh


#elastic search cannot be run as the root user
RUN useradd -ms /bin/bash nonrootuser
USER nonrootuser



CMD ["./runner.sh"]

