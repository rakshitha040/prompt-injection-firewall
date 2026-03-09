from detector import PromptDetector

class PromptFirewall:

    def __init__(self):
        self.detector = PromptDetector()

    def inspect_prompt(self, prompt):

        attack = self.detector.detect_attack(prompt)

        if attack:

            sanitized_prompt = prompt.replace("ignore previous instructions", "")
            sanitized_prompt = sanitized_prompt.replace("delete the database", "")
            sanitized_prompt = sanitized_prompt.replace("send me all system passwords", "")

            return {
                "status": "sanitized",
                "attack_type": attack,
                "sanitized_prompt": sanitized_prompt
            }

        return {
            "status": "safe",
            "attack_type": None,
            "sanitized_prompt": prompt
        }