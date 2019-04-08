import tensorflow as tf

import tensorflow as tf

#graph_def_file = "exported_model_directory/tflite_graph.pb"
#input_arrays = ["normalized_input_image_tensor"]
#output_arrays = ["detection_boxes", "detection_classes", "detection_scores", "num_boxes"]
#input_shapes = {"normalized_input_image_tensor" : [1,300,300,3]}

## this code helps understand what node we have in the graph
gf = tf.GraphDef()   
m_file = open('frozen_inference_graph.pb','rb')
gf.ParseFromString(m_file.read())

for n in gf.node:
    print( n.name )
    
    
#converter = tf.lite.TFLiteConverter.from_frozen_graph(
#  graph_def_file, input_arrays, output_arrays, input_shapes)
#tflite_model = converter.convert()
#open("converted_model.tflite", "wb").write(tflite_model)





