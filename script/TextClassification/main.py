# -*- coding: utf-8 -*-
from data_loader import load_data_db
import pandas as pd
import numpy as np
import pymysql
import os
import csv
import json
import numpy as np
import pandas as pd
import pickle as pkl
import tensorflow as tf
from tensorflow.contrib import learn
import urllib
import requests

import data_loader

# Show warnings and errors only
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
# File paths
tf.flags.DEFINE_string('output_data_file', None, '''Output data file path''')
tf.flags.DEFINE_string('model_dir', None, '''Restore the model from this run''')
tf.flags.DEFINE_string('params_dir', None, '''Restore the model from this run''')
# tf.flags.DEFINE_string('checkpoint', 'clf', '''Restore the graph from this checkpoint''')
# Test batch size
tf.flags.DEFINE_integer('batch_size', 64, 'Test batch size')
FLAGS = tf.flags.FLAGS
def main(_):
    print("******推断程序开始******")
    db=pymysql.connect(
       host='127.0.0.1',
       user='root',
       passwd='zhanghongyu',
       db='EP2',
       charset='utf8',
       port=3306,
       autocommit=True
    )

    #Restore parameters
    with open(os.path.join(FLAGS.params_dir,'params.pkl'), 'rb') as f:
        params = pkl.load(f, encoding='bytes')
    # Restore vocabulary processor
    vocab_processor = learn.preprocessing.VocabularyProcessor.restore(os.path.join(FLAGS.params_dir, 'vocab'))


    if not os.path.exists(FLAGS.output_data_file):
        os.mknod(FLAGS.output_data_file)

    # Load test data
    data, times,lengths, _ = data_loader.load_data_db(db,
                                                    sw_path=params['stop_word_file'],
                                                    min_frequency=params['min_frequency'],
                                                    max_length=params['max_length'],
                                                    language=params['language'],
                                                    vocab_processor=vocab_processor,
                                                     shuffle=False)

    feed_dict={'input_x':data.tolist(),"input_y":[0]*len(data.tolist())}
    # data_loader = MNISTLoader()
    data = json.dumps({
        # 'signature_name':["input_x","input_y"],
        "instances": feed_dict
        })
    headers = {"content-type": "application/json"}
    json_response = requests.post(
        'http://localhost:8501/v1/models/model:predict',
        data=data, headers=headers)
    with open('predictions.json', 'w') as f:
        f.write(json.dumps(json_response.json()))
    predictions = json_response.json()['predictions'][0]
    id=[i for i in range(lengths)]
    df=pd.DataFrame({'id':id,'label':predictions,'time':times})
    df.to_csv(FLAGS.output_data_file)
    print('Predictions saved to {}'.format(FLAGS.output_data_file))
    
    # # Restore graph
    # graph = tf.Graph()
    # with tf.Session(graph=tf.Graph()) as sess:
    #     sess = tf.Session()

    #     tf.saved_model.loader.load(sess, ['serve'], FLAGS.model_dir)
    #     graph = tf.get_default_graph()

    #     # Get tensors
    #     input_x = graph.get_tensor_by_name('input_x:0')
    #     input_y = graph.get_tensor_by_name('input_y:0')
    #     keep_prob = graph.get_tensor_by_name('keep_prob:0')
    #     predictions = graph.get_tensor_by_name('softmax/predictions:0')
    #     accuracy = graph.get_tensor_by_name('accuracy/accuracy:0')

    #     # Generate batches
    #     batches = data_loader.batch_iter_db(data, lengths, FLAGS.batch_size, 1)

    #     num_batches = int(len(data)/FLAGS.batch_size)
    #     all_predictions = []
    #     # Test
    #     for batch in batches:
    #         x_test,dummy,x_lengths = batch
    #         if params['clf'] == 'cnn':
    #             feed_dict = {input_x: x_test, input_y: dummy, keep_prob: 1.0}
    #             batch_predictions, _ = sess.run([predictions, accuracy], feed_dict)
    #         else:
    #             batch_size = graph.get_tensor_by_name('batch_size:0')
    #             sequence_length = graph.get_tensor_by_name('sequence_length:0')
    #             feed_dict = {input_x: x_test, input_y: dummy, batch_size: FLAGS.batch_size, sequence_length: x_lengths, keep_prob: 1.0}

    #             batch_predictions, _ = sess.run([predictions, accuracy], feed_dict)
    #         all_predictions = np.concatenate([all_predictions, batch_predictions])




    # # Save all predictions
    # with open(FLAGS.output_data_file, 'w', encoding='utf-8', newline='') as f:
    #     csvwriter = csv.writer(f)
    #     csvwriter.writerow(['id','label','time'])
    #     for i,time in zip(range(len(all_predictions)),times):
    #         csvwriter.writerow([i,all_predictions[i],time])
    #     print('Predictions saved to {}'.format(FLAGS.output_data_file))

    print("成功完成推断!")


    cursor=db.cursor()
    cursor.execute('use EP2')
    cursor.execute(""" set sql_mode=""; """)
    cursor.execute(r""" load data infile '/var/lib/mysql-files/testy.csv' into table flow FIELDS TERMINATED BY ','  OPTIONALLY
 ENCLOSED BY '"'  LINES TERMINATED BY '\n'; """) 
    print("成功将推断结果写入数据库!")
    db.close()































if __name__ =="__main__":
    tf.app.run()
