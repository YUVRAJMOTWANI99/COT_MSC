from llama_index.core.llama_pack import download_llama_pack
from llama_index.llms.openai import OpenAI

MixSelfConsistencyPack = download_llama_pack(
    "MixSelfConsistencyPack", "./mix_self_consistency_pack"
)

from mix_self_consistency_pack.llama_index.packs.tables.mix_self_consistency.base import MixSelfConsistencyQueryEngine

llm = OpenAI(model="gpt-3.5-turbo-0125" , api_key='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')
import pandas as pd

df = pd.read_csv("11.csv")
query_engine = MixSelfConsistencyQueryEngine(df=df, llm=llm, verbose=True)

response = query_engine.query(
    "Who won best Director in the 1972 Academy Awards?"
)