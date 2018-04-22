
import * as tf from '@tensorflow/tfjs';
import {
  loadFrozenModel
} from '@tensorflow/tfjs-converter';

const text = document.getElementById('inwindow');
const INPUT_NODE_NAME = 'x';
const OUTPUT_NODE_NAME = 'y';

const weight = 2;

const num = Math.floor(Math.random()*100)


const loadandrun = async () => {

  console.log("loading")
  const MODEL_URL = 'tensorflowjs_model.pb';
  const WEIGHTS_URL = 'weights_manifest.json';

  const model = await loadFrozenModel(MODEL_URL, WEIGHTS_URL);
  model.executor._weightMap.w[0]=tf.scalar(weight)
  console.log(model.executor._weightMap.w[0].dataSync()[0])

  console.log("loaded")
  text.innerHTML = "Loaded!"

  const dict = {};
  dict[INPUT_NODE_NAME] = tf.scalar(num);
  console.log(model)

  text.innerHTML = weight+ " times " + num + " is: " + model.execute(dict, OUTPUT_NODE_NAME).dataSync();
}

loadandrun();
