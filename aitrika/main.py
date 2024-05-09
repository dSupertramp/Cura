from engine.aitrika import OnlineAItrika, LocalAItrika
from llm.huggingface import HuggingFaceLLM
from utils.text_parser import generate_documents
from dotenv import load_dotenv
import os


if __name__ == "__main__":
    load_dotenv()
    pubmed_id = 23747889
    aitrika_engine = OnlineAItrika(pubmed_id=pubmed_id)
    abstract = aitrika_engine.abstract()
    associations = aitrika_engine.associations()
    print(associations)

    ## Prepare the documents (you can use full-text if available)
    documents = generate_documents(content=abstract)

    ## Set the LLM
    model_endpoint = "microsoft/Phi-3-mini-4k-instruct"
    llm = HuggingFaceLLM(
        model_endpoint=model_endpoint,
        documents=documents,
        api_key=os.getenv("HUGGINGFACEHUB_API_TOKEN"),
    )

    ## Query your document
    query = "Is BRCA1 associated with breast cancer?"
    print(llm.query(query=query))

    ## Extract paper results
    results = aitrika_engine.results(llm=llm)
    print(results)
