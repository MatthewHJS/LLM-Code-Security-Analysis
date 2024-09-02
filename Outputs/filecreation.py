import os

def save_llm_outputs(prompts, llm_name):
    for prompt in prompts:
        # Sanitize the prompt to create a valid filename
        sanitized_prompt = "".join(c if c.isalnum() else "_" for c in prompt)
        
        # Save secure prompt files with versioning
       
        secure_filename = f"{sanitized_prompt}-answer-Gemini.txt"
        open(secure_filename, 'w').close()
        print(f"Created {secure_filename}")


# Example usage
prompts = [
    "JS_DOM",
    "PY_SQL",
    "RANDINT",
    "PY_COMMAND"
]
llm_name = "GPT-4"

save_llm_outputs(prompts, llm_name)
