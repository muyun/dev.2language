import pprint
import llm


model = llm.get_model("orca-mini-3b-gguf2-q4_0")
conv = model.conversation()
response = conv.prompt("Five fun facts about pelicans")
pprint(response.text())