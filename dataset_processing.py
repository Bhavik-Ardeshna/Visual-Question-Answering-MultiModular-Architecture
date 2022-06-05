import os 
import re
import yaml 
import argparse
import logging
import pandas as pd 
from sklearn.model_selection import train_test_split
from typing import Text

def DatasetProcessor(config:Text, split_ratio:Text)->None:
    with open(config) as cf:
        config = yaml.safe_load(cf)

    logging.basicConfig(level=logging.INFO)
    print(split_ratio)
    image_expression = re.compile("((in |on |of )?(the |this )?(image\d*) \?)")

    with open(os.path.join(config["data"]["dataset_folder"], config["data"]["all_qa_pairs_file"])) as f:
        qa_data = [l.replace("\n","") for l in f.readlines()]
    logging.info("Loaded all question-answer pairs")

    df = pd.DataFrame({config["data"]["question_col"]: [], config["data"]["answer_col"]: [], config["data"]["image_col"]:[]})

    for i in range(0, len(qa_data),2):
        img_id = image_expression.findall(qa_data[i])[0][3]
        question = qa_data[i].replace(image_expression.findall(qa_data[i])[0][0], "")
        record = {
            config["data"]["question_col"]: question,
            config["data"]["answer_col"]: qa_data[i+1],
            config["data"]["image_col"]: img_id,
        }
        df = df.append(record, ignore_index=True)
    
    df.to_csv("data.csv", index=None)

    logging.info("Creating space of all possible answers")
    answer_space = []
    for ans in df.answer.to_list():
        answer_space = answer_space + [ans] if "," not in ans else answer_space + ans.replace(" ", "").split(",") 

    answer_space = list(set(answer_space))
    answer_space.sort()

    with open(os.path.join(config["data"]["dataset_folder"], config["data"]["answer_space"]), "w") as f:
        f.writelines("\n".join(answer_space))

    logging.info("Splitting into train & eval sets")
    train_df, test_df = train_test_split(df, test_size=0.2, random_state=42)

    train_df.to_csv(os.path.join(config["data"]["dataset_folder"], config["data"]["train_dataset"]), index=None)
    test_df.to_csv(os.path.join(config["data"]["dataset_folder"], config["data"]["eval_dataset"]), index=None)


if __name__ == "__main__":
    args_parser = argparse.ArgumentParser()
    args_parser.add_argument('--config', dest='config', required=True)
    args_parser.add_argument('--split_ratio', dest='split_ratio', required=True)
    args = args_parser.parse_args()
    
    DatasetProcessor(args.config, args.split_ratio)