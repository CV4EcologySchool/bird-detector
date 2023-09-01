from comet_ml import Experiment
import ultralytics
from ultralytics import YOLO
import yaml

# # Load the default config
# cfg = ultralytics.cfg.get_cfg(cfg='default.yaml') # or could name it as config.yaml

# comet_api_key = cfg.api_key
# project_name = cfg.project_name

# # Create the Experiment
# experiment = Experiment(api_key=comet_api_key, 
#                         project_name=project_name)

# experiment_name = cfg.experiment_name
# experiment.set_name(experiment_name)

# # Convert the config to a dictionary for logging
# comet_cfg = ultralytics.cfg.cfg2dict(cfg)

# # Log the experiment parameters
# experiment.log_parameters(comet_cfg)

# # Create an artifact for the dataset
# artifact = experiment.create_artifact(
#     "yolov8-data",
#     artifact_type="dataset"
# )

# # Add the directory containing the data to the artifact
# artifact.add_dir("runs/")

# # Log the artifact
# experiment.log_artifact(artifact)

# # Load the pretrained model
# model = YOLO(comet_cfg['model'])

# # Watch the model for automatic logging (optional)
# # model.watch(experiment, log="all", log_freq=5, log_graph=True)

# # Train the model
# results = model.train(cfg='default.yaml', name=experiment.get_key())

# # Validate the model
# metrics = model.val()

# # # End the CometML experiment
# # experiment.end()
# import comet_ml
# from comet_ml import Experiment  
# import ultralytics
# from ultralytics import YOLO
# import yaml

# # # CometML
# # # Comet ML experiment saving details
# # experiment_name: bird_detector_round1
# # # add the scheduler step
# # project_name: cagedbird-classifier
# # api_key: 6D79SKeAIuSjteySwQwqx96nq

# comet_ml.init(api_key=6D79SKeAIuSjteySwQwqx96nq, 
#               project_name='comet-example-yolov5')


# # Initialize CometML
# comet_ml.init(api_key="YOUR_API_KEY", project_name="your-project")

# # Load experiment config
# cfg = ultralytics.cfg.get_cfg(cfg='default.yaml')
# experiment_name = cfg.experiment_name 

# # Create Comet experiment
# experiment = comet_ml.Experiment(project_name="your-project")
# experiment.set_name(experiment_name)

# # Log parameters
# experiment.log_parameters(cfg)

# # Create YOLO model
# model = YOLO(cfg.model)

# # Train model  
# results = model.train(data="data.yaml")

# # Validate model
# metrics = model.val()

# # End Comet experiment
# experiment.end()


# Load experiment config
cfg = ultralytics.cfg.get_cfg(cfg='default.yaml')

# Create YOLO model
model = YOLO(cfg.model)

# Train model
results = model.train(data="dataset.yaml")

# Validate model
metrics = model.val()

# yolo predict model=yolov8n-seg.pt source='https://ultralytics.com/images/bus.jpg' imgsz=320