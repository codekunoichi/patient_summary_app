from app.openai_model import OpenAIModel
from app.anthropic_model import AnthropicModel
from app.visit_summary import VisitSummary
from app.prompt_generator import BillerPrompter, SummarizeChartPrompter, DiagnosisCodePrompter
class ModelOrchestrator:
    def __init__(self, model_type: str, prompter_type: str):
        print(f"************* Summarization for {model_type} for the persona {prompter_type}")
        if prompter_type == 'biller':
            self.prompter = BillerPrompter()
        elif prompter_type == 'summarizer':
            self.prompter = SummarizeChartPrompter()
        elif prompter_type == 'diagnosis':
            self.prompter = DiagnosisCodePrompter()
        else:
            raise ValueError("Invalid prompter type provided. Choose 'biller' or 'summarizer'.")

        if model_type == 'openai':
            self.model = OpenAIModel(self.prompter)
        elif model_type == 'anthropic':
            self.model = AnthropicModel(self.prompter)
        else:
            raise ValueError("Invalid model type provided. Choose 'openai' or 'anthropic'.")

    def process(self, visit_summary: VisitSummary, ) -> str:
        # Call the model with the generated prompt
        result = self.model.call_model(visit_summary.get_sample_visits())
        return result
    
    # removes the markdown characters returned.
    def process_pretty(self, visit_summary: VisitSummary, ) -> str:
        # Call the model with the generated prompt
        result = self.model.call_model_and_scrub(visit_summary.get_sample_visits())
        return result

if __name__ == "__main__":
    # Example usage
    visit_summary = VisitSummary(VisitSummary.get_sample_visits())

    # Orchestrate with OpenAI model and BillerPrompter
    orchestrator = ModelOrchestrator(model_type='openai', prompter_type='biller')
    result = orchestrator.process_pretty(visit_summary)
    print(result)

    # Orchestrate with Anthropic model and BillerPrompter
    orchestrator = ModelOrchestrator(model_type='anthropic', prompter_type='biller')
    result = orchestrator.process_pretty(visit_summary)
    print(result)

    # Orchestrate with OpenAI model and SummarizeChartPrompter
    orchestrator = ModelOrchestrator(model_type='openai', prompter_type='summarizer')
    result = orchestrator.process_pretty(visit_summary)
    print(result)

    # Orchestrate with Anthropic model and SummarizeChartPrompter
    orchestrator = ModelOrchestrator(model_type='anthropic', prompter_type='summarizer')
    result = orchestrator.process_pretty(visit_summary)
    print(result)

    # Orchestrate with Anthropic model and DiagnosisCodePrompter
    orchestrator = ModelOrchestrator(model_type='anthropic', prompter_type='diagnosis')
    result = orchestrator.process_pretty(visit_summary)
    print(result)

    # Orchestrate with OpenAI model and DiagnosisCodePrompter
    orchestrator = ModelOrchestrator(model_type='openai', prompter_type='diagnosis')
    result = orchestrator.process_pretty(visit_summary)
    print(result)