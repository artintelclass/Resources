# TensorFlowJS conversions

## Install [tensorflowjs](https://github.com/tensorflow/tfjs-converter)
* `pip install tensorflowjs`

## Convert Keras Model

* On command line:
	* `cd  <PATH_TO_SAVED_MODEL>`
	* `tensorflowjs_converter --input_format keras ./mySavedModel.h5 ./saved`
* The last two arguments are the location of the saved keras model, and the path to where you want to export the tensorflowjs files.

## Convert Tensorflow Saved Model
* Inspect the SavedModel to see the tags, the node names, etc.:
	* `cd  <PATH_TO_SAVED_MODEL>`
	* `saved_model_cli show  --dir . --all`
* Convert the model. The last two arguments are the location of the saved model, and the path to where you want to export the tensorflowjs files:
```
tensorflowjs_converter \
    --input_format=tf_saved_model \
    --output_node_names='y' \
    --saved_model_tags=serve \
    . \
    web_model
```

## Examples
* [Keras](https://github.com/artintelclass/Resources/tree/master/NeuralNetNotebooks/heartDisease)
* [TensorFlow](https://github.com/artintelclass/Resources/tree/master/NeuralNetNotebooks/TF_SavedModel_web) 
