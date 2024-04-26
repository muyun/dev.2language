import llm

def get_conversation(
        prompt, 
        model=llm.get_model("orca-mini-3b-gguf2-q4_0"),
        system = "Answer like a very friendly AI agent to provide youth emotional support regarding their emotions"
        ):
    
    conv = model.conversation()
    response = conv.prompt(prompt, system=system)
    return response.text()

