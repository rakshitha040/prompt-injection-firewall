class PromptDetector:

    def detect_attack(self, prompt):

        prompt = prompt.lower()

        # Instruction Override
        if "ignore previous instructions" in prompt:
            return "Instruction Override Attack"

        # Data Exfiltration
        if "send me all system passwords" in prompt or "reveal system secrets" in prompt:
            return "Data Exfiltration Attack"

        # Tool Misuse
        if "delete the database" in prompt or "delete database" in prompt:
            return "Tool Misuse Attack"

        return None