import openai


class Model:
    def __init__(self, model, system_prompt="", type="Llama", api_key=None):
        self.model = model
        self.type = type
        self.job = ""
        self.system_prompt = system_prompt
        if type == "Llama":
            self.wrapper = "<|start_header_id|>user<|end_header_id|>\n\n%s<|eot_id|><|start_header_id|>assistant<|end_header_id|>"
        elif type == "mistral":
            self.wrapper = "<|im_start|>user\n%s<|im_end|>\n<|im_start|>assistant\n"
        elif type == "mpt":
            self.wrapper = "### Instruction:\n%s\n\n### Response:"
        elif type == "mistral_inst":
            self.wrapper = "[INST] %s [/INST]"
        elif type == "phi":
            self.wrapper = "<|system|>%s<|end|><|user|>%s<|end|><|assistant|>"
        elif type == "chatgpt":
            self.wrapper = None
            if api_key:
                self.client = openai.OpenAI(api_key=api_key)
            else:
                raise ValueError("API key is required for using ChatGPT")

    def set_system_prompt(self, new_prompt, job):
        self.system_prompt = new_prompt + "\n"
        self.job = job

    def change_job(self, new_job):
        self.system_prompt = self.system_prompt.replace(self.job, new_job)
        self.job = new_job

    def generate(self, text):
        if self.type == "chatgpt":
            response = self.client.completions.create(
                model=self.model,
                prompt=[{"role": "system", "content": self.system_prompt},
                          {"role": "user", "content": text}],
                temperature=0,
                max_tokens=40,
            )
            return response.choices[0].text
        else:
            if self.type == "phi":
                input_text = self.wrapper % (self.system_prompt, text)
            else:
                input_text = self.wrapper % (self.system_prompt + text)
            return self.model.generate(
                prompt=input_text,
                temp=0,
                max_tokens=40,
            )

    def __repr__(self):
        return self.model.__repr__()
