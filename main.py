import os
import yaml
import argparse
import logging
import json
from typing import Text
import torch
import transformers

from multimodal_collator import createMultimodalDataCollator
from loader import loadQADataset
from model import createMultimodalModelForVQA
from trainer import trainMultimodalModelForVQA
from modal_evaluator import VQAScoreCalculator
from util import countTrainableParameters

def main(config_path: Text) -> None:
    transformers.logging.set_verbosity_error()
    logging.basicConfig(level=logging.INFO)
    
    with open(config_path) as conf_file:
        config = yaml.safe_load(conf_file)
    
    if config["base"]["use_cuda"]:
        device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
        os.environ['CUDA_VISIBLE_DEVICES'] = '0' # SET ONLY 1 GPU DEVICE
    else:
        device =  torch.device('cpu')

    data = loadQADataset(config)
    logging.info("Loaded processed VQA Dataset")

    multimodal_collator = createMultimodalModelForVQA(config)
    logging.info("Created data collator")

    multimodal_model = createMultimodalModelForVQA(config, data['answer_space']).to(device)
    logging.info("Initialized multimodal model for VQA")

    modal_calculator = VQAScoreCalculator(data['answer_space'])

    logging.info("Training started...")
    training_metrics, eval_metrics = trainMultimodalModelForVQA(
        config, device, data["dataset"], 
        multimodal_collator, multimodal_model,
        modal_calculator.compute_metrics
    )

    logging.info("Training complete")
    
    os.makedirs(config["metrics"]["metrics_folder"], exist_ok=True)

    metrics = {**training_metrics[2], **eval_metrics}
    metrics["num_params"] = countTrainableParameters(multimodal_model)
    
    metrics_path = os.path.join(config["metrics"]["metrics_folder"], config["metrics"]["metrics_file"])
    json.dump(
        obj=metrics,
        fp=open(metrics_path, 'w'),
        indent=4
    )
    logging.info("Metrics saved")


if __name__ == '__main__':
    args_parser = argparse.ArgumentParser()
    args_parser.add_argument('--config', dest='config', required=True)
    args = args_parser.parse_args()
    
    main(args.config)

    