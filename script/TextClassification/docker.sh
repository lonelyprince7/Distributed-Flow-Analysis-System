docker run -p 8501:8501 \
  --mount type=bind,source=/home/lonelyprince7/LocalCode/TextClassification/model,target=/models/model \
  -e MODEL_NAME=model -t tensorflow/serving &