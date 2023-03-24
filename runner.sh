#!/bin/bash

# # Check that the Elasticsearch binary exists and is executable
# if [ ! -x ./elasticsearch-7.9.2/bin/elasticsearch ]; then
#     echo "Error: Elasticsearch binary not found or not executable"
#     exit 1
# fi

# # Start Elasticsearch
# echo "Starting Elasticsearch"
# ./elasticsearch-7.9.2/bin/elasticsearch &

# # Wait for Elasticsearch to start up (adjust as needed)
# while ! nc -z localhost 9200; do
#   sleep 1
# done

# # Check that Elasticsearch is running by making a request to the API
# curl -s localhost:9200 >/dev/null
# if [ $? -ne 0 ]; then
#     echo "Error: Failed to start Elasticsearch"
#     exit 1
# fi

# # Run Python script
# echo "Starting Python script"
# python3 app/trial.py

# Check that the Elasticsearch binary exists and is executable
# if [ ! -x ./elasticsearch-7.9.2/bin/elasticsearch ]; then
#     echo "Error: Elasticsearch binary not found or not executable"
#     exit 1
# fi


# Start Elasticsearch
echo "Starting Elasticsearch"
./elasticsearch-7.9.2/bin/elasticsearch &

# Wait for Elasticsearch to start up (fixed wait time of 10 seconds)
echo "Waiting for Elasticsearch to start up"
sleep 300

# Run Python script
echo "Starting flask server"
python3 app.py