from detector import PromptDetector

class PromptFirewall:

    def __init__(self):
        self.detector = PromptDetector()

    def inspect_prompt(self, prompt):

        attack = self.detector.detect_attack(prompt)

        if attack:
            return {
                "status": "blocked",
                "attack_type": attack,
                "message": "Prompt blocked by firewall"
            }

        return {
            "status": "safe",
            "attack_type": None,
            "message": "Prompt allowed"
        }