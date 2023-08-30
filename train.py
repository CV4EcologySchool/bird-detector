from ultralytics import YOLO
import ultralytics
from comet_ml import Experiment

# Initialize a CometML experiment
experiment = Experiment(
    project_name="your-project-name",
    workspace="your-workspace",
    auto_output_logging="native"
)

# Load the default config
cfg = ultralytics.cfg.get_cfg(cfg='default.yaml')

# Convert the config to a dictionary for logging
comet_cfg = ultralytics.cfg.cfg2dict(cfg)

# Log the experiment parameters
experiment.log_parameters(comet_cfg)

# Create an artifact for the dataset
artifact = experiment.create_artifact(
    "yolov8-data",
    artifact_type="dataset"
)

# Add the directory containing the data to the artifact
artifact.add_dir("runs/")

# Log the artifact
experiment.log_artifact(artifact)

# Load the pretrained model
model = YOLO(comet_cfg['model'])

# Watch the model for automatic logging (optional)
# model.watch(experiment, log="all", log_freq=5, log_graph=True)

# Train the model
results = model.train(cfg='default.yaml', name=experiment.get_key())

# Validate the model
metrics = model.val()

# End the CometML experiment
experiment.end()
