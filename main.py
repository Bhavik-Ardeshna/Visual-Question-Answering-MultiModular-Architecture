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