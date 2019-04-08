tflite_convert \
  --output_file=detect.tflite \
  --graph_def_file=exported_model_directory/tflite_graph.pb \
  --input_arrays=normalized_input_image_tensor \
  --output_arrays=TFLite_Detection_PostProcess,TFLite_Detection_PostProcess:1,TFLite_Detection_PostProcess:2,TFLite_Detection_PostProcess:3
  --input_shape=1,300,300,3


bazel run -c opt tensorflow/contrib/lite/toco:toco -- \ --input_file=C:/tensorflow1/models/research/object_detection/inference_graph_region_detection/exported_model_directory/tflite_graph.pb \ --output_file=C:/tensorflow1/models/research/object_detection/inference_graph_region_detection/exported_model_directory/detect.tflite \ --input_shapes=1,300,300,3 \ --input_arrays=normalized_input_image_tensor \ --output_arrays='TFLite_Detection_PostProcess','TFLite_Detection_PostProcess:1','TFLite_Detection_PostProcess:2','TFLite_Detection_PostProcess:3' \ --inference_type=QUANTIZED_UINT8 \ --mean_values=128 \ --std_values=128 \ --change_concat_input_ranges=false \ --allow_custom_ops


tflite_convert \
  --output_file=detect.tflite \
  --graph_def_file=frozen_inference_graph.pb \
  --input_arrays=image_tensor \
  --output_arrays=detection_boxes,detection_scores,detection_classes,num_detections
  --input_shape=1,300,300,3
