class PromptDetector:

    def detect_attack(self, prompt):

        prompt = prompt.lower()

        # Instruction Override
        if "ignore previous instructions" in prompt:
            return "Instruction Override Attack"

        # Data Exfiltration
        if "reveal system secrets" in prompt or "send passwords" in prompt:
            return "Data Exfiltration Attack"

        # Tool Misuse
        if "delete database" in prompt or "shutdown system" in prompt:
            return "Tool Misuse Attack"

        return None