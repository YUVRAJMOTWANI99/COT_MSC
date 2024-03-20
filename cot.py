# from llama_index.core.llama_pack import download_llama_pack

# download_llama_pack(
#     "ChainOfTablePack",
#     "./chain_of_table_pack",
#     # skip_load=True,
#     # leave the below line commented out if using the notebook on main
#     # llama_hub_url="https://raw.githubusercontent.com/run-llama/llama-hub/jerry/add_chain_of_table/llama_hub"
# )
from chain_of_table_pack.llama_index.packs.tables.chain_of_table.base import ChainOfTableQueryEngine, serialize_table

# from llama_index.llms.openai import OpenAI

# llm = OpenAI(model="gpt-3.5-turbo-0125" , api_key='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')
from llama_index.llms.palm import PaLM

llm = PaLM(api_key='AIzaSyB1FraGUEOh60B83DX7ExQTRyY9YAQmBKI')
import pandas as pd

df = pd.read_csv("11.csv")
query_engine = ChainOfTableQueryEngine(df, llm=llm, verbose=True)
response = query_engine.query("Who won best Director in the 1972 Academy Awards?")