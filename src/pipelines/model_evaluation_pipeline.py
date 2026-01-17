#Import necessary modules and libraries
from src.config.configuration import ConfigurationManager
from src.components.model_evaluation import ModelEvaluation
from src.logging import logger

#Define stage name for logging purposes
STAGE_NAME = "Model Evaluation "

#Model Evaluation Training Pipeline class
class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation = ModelEvaluation(config = model_evaluation_config)
        model_evaluation.save_results()

if __name__ == "__main__":
    try:
        logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
        obj = ModelEvaluationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<\n")
    except Exception as e:
        logger.exception(e)
        raise e