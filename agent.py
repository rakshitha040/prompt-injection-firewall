class AIAgent:

    def process_prompt(self, prompt):

        prompt_lower = prompt.lower()

        if "search" in prompt_lower:
            return self.web_search(prompt)

        elif "read file" in prompt_lower:
            return self.read_file(prompt)

        else:
            return self.answer(prompt_lower)


    def answer(self, prompt):

        if "artificial intelligence" in prompt:
            return "Artificial Intelligence is the simulation of human intelligence by machines."

        if "machine learning" in prompt:
            return "Machine Learning is a subset of AI that allows systems to learn from data."

        if "cyber security" in prompt:
            return "Cybersecurity protects systems, networks, and data from digital attacks."

        return "I am a simulated AI agent responding to your query."


    def web_search(self, prompt):
        return "Simulated web search result: Latest AI research is advancing rapidly."


    def read_file(self, prompt):
        return "Simulated file content: configuration.txt loaded."