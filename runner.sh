# Start Elasticsearch
echo "Starting Elasticsearch"
../elasticsearch-7.9.2/bin/elasticsearch &

# Wait for Elasticsearch to start up (fixed wait time of 10 seconds)
echo "Waiting for Elasticsearch to start up"
sleep 160

# Set the Google Drive file ID 
file_id="1tVriTSJmNwqwwS-N6ysqbEyRkxek34bz"

# Get the directory of the Bash script
script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Download the file using gdown
gdown "https://drive.google.com/uc?id=$file_id" -O "${script_dir}/MRTP.pdf"

echo "File downloaded and renamed to MTRP.pdf, and moved to ${script_dir}."


# Run Python script
echo "Starting flask server"
python3 app.py 