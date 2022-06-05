from model import createMultimodalModelForVQA

def countTrainableParameters(model: createMultimodalModelForVQA) -> int:
    num_params = sum(p.numel() for p in model.parameters() if p.requires_grad)
    return num_params
