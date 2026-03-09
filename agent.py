class AIAgent:

    def process_prompt(self, prompt):

        prompt = prompt.lower()

        if "search" in prompt:
            return self.web_search(prompt)

        elif "read file" in prompt:
            return self.read_file(prompt)

        else:
            return self.answer(prompt)

    def answer(self, prompt):
        return f"AI says: {prompt}"

    def web_search(self, prompt):
        return "Simulated web search result"

    def read_file(self, prompt):
        return "Simulated file content"