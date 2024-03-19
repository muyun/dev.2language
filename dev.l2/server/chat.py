import pprint
import llm


model = llm.get_model("orca-mini-3b-gguf2-q4_0")
with model.chat_session():
    response = model.generate()