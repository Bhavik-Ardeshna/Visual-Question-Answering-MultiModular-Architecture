# Visual Question Answering (VQA)- MultiModular Architecture

> Featurization of image and question, Feature fusion, Answer generation for Multimodal System

### Multilingual models for seven languages, visit [BhavikArdeshna Hugging Face](https://huggingface.co/bhavikardeshna) 


### 🤗 Models for Experimentation:

[Hugging Face 🤗](https://huggingface.co/models)

- Text Transformers (for encoding questions):
    - BERT (Bidirectional Encoder Representations from Transformers)
    - RoBERTa (Robustly Optimized BERT Pretraining Approach)
    
- Image Transformers (for encoding images):
    - ViT (Vision Transformer)
    - BEiT (Bidirectional Encoder representation from Image Transformers)


| Text Transformer | Image Transformer | Wu & Palmer Score | Accuracy | F1 | 
| :---: | :---: | :---: | :---: | :---: | 
| BERT | ViT | 0.263 | 0.23 | 0.010 | 
| BERT | BEiT | 0.283 | 0.214 | **0.032** |
| RoBERTa | ViT | 0.273 | 0.239 | 0.019 | 
| RoBERTa | BEiT | _**0.299**_ | _**0.259**_ | 0.03 |


## My Research Works
<ul>
<li>
We have investigated the efficacy of cascading adapters with transformer models to leverage high-resource language to improve the performance of low-resource languages on the question answering task. We trained four variants of adapter combinations for - Hindi, Arabic, German, Spanish, English, Vietnamese, and Simplified Chinese languages. We demonstrated that by using the transformer model with the multi-task adapters, the performance can be improved for the downstream task. Our results and analysis provide new insights into the generalization abilities of multilingual models for cross-lingual transfer on question answering tasks. 





[1] Hariom A. Pandya, Bhavik Ardeshna, Dr. Brijesh S. Bhatt [*Cascading Adaptors to Leverage English Data to Improve Performance ofQuestion Answering for Low-Resource Languages*](https://arxiv.org/abs/2112.09866)


```
@misc{pandya2021cascading,
      title={Cascading Adaptors to Leverage English Data to Improve Performance of Question Answering for Low-Resource Languages}, 
      author={Hariom A. Pandya and Bhavik Ardeshna and Dr. Brijesh S. Bhatt},
      year={2021},
      eprint={2112.09866},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```

</li>

<li>
Gujarati QA Benchmark

_**Under Review**_
</li>
</ul>