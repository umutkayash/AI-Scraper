from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template = (
    "You are tasked with extracting specific information from the following text content: {dom_content}. "
    "Please follow these instructions carefully: \n\n"
    "1. **Extract Information:** Only extract the information that directly matches the provided description: {parse_description}. "
    "2. **No Extra Content:** Do not include any additional text, comments, or explanations in your response. "
    "3. **Empty Response:** If no information matches the description, return an empty string ('')."
    "4. **Direct Data Only:** Your output should contain only the data that is explicitly requested, with no other text."
)

ollama_model = OllamaLLM(model="llama3")


def extract_data(dom_chunks, detail_description):
    prompt_template = ChatPromptTemplate.from_template(template)
    processing_chain = prompt_template | ollama_model

    extraction_results = []

    for index, content_segment in enumerate(dom_chunks, start=1):
        result = processing_chain.invoke(
            {"dom_content": content_segment, "parse_description": detail_description}
        )
        print(f"Processing segment: {index} of {len(dom_chunks)}")
        extraction_results.append(result)

    return "\n".join(extraction_results)
