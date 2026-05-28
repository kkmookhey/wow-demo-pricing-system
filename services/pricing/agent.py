"""Pricing recommendation agent.

Uses langchain to wrap an LLM-driven pricing suggestion behind a stable
interface. Called from the FastAPI routes in main.py.
"""
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI


def make_pricing_chain() -> LLMChain:
    prompt = PromptTemplate(
        input_variables=["product"],
        template="What is the recommended price for {product}? Reply with a single USD number.",
    )
    llm = OpenAI(temperature=0.2)
    return LLMChain(llm=llm, prompt=prompt)


def suggest_price(product: str) -> str:
    chain = make_pricing_chain()
    return chain.run(product=product)
