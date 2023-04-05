from langchain import LLMChain, PromptTemplate
from inspect import signature

def use_prompt(fn):
    sig = signature(fn)
    args = {x.name: '{' + x.name + '}' for x in sig.parameters.values()}
    tmpl = fn(**args)
    return PromptTemplate(
        input_variables=list(args.keys()), template=tmpl
    )

def use_llm(provider):
    def _use_llm(prompt):
        return LLMChain(llm=provider, prompt=prompt)
    return _use_llm
