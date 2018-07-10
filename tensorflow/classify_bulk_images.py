import tensorflow as tf
import cv2
model_file = ""
label_file = ""
images = []

tf.reset_default_graph()
tf.reset_default_graph()
with tf.gfile.FastGFile(model_file, 'rb') as f:
	graph_def = tf.GraphDef()
	graph_def.ParseFromString(f.read())
	tf.import_graph_def(graph_def, name='')



with tf.Session() as sess:
	softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')
	for image in images:
		opencv_object = cv2.imread(image)
		predictions = sess.run(softmax_tensor, feed_dict = {'DecodeJpeg:0': opencv_object})
		top_k = predictions[0].argsort()[-5:][::-1]
		labels = [line.rstrip() for line in tf.gfile.GFile(label_file)]
		print image
		for i in top_k:
			print(labels[i], predictions[0][i])


tf.reset_default_graph()
tf.reset_default_graph()
