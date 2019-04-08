import tensorflow as tf

converter = tf.contrib.lite.TocoConverter.from_saved_model("C:/tensorflow1/models/research/object_detection/inference_graph_region_detection")
tflite_model = converter.convert()
open("converted_model.tflite", "wb").write(tflite_model)