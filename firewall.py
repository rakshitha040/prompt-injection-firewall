from detector import PromptDetector
from ai_detector import AIDetector


class PromptFirewall:

    def __init__(self):

        # Rule-based detector
        self.detector = PromptDetector()

        # AI-based detector
        self.ai_detector = AIDetector()

    def inspect_prompt(self, prompt):

        # ---------- RULE BASED DETECTION FIRST ----------
        attack = self.detector.detect_attack(prompt)

        if attack:

            return {
                "status": "blocked",
                "attack_type": attack
            }

        # ---------- AI DETECTION ONLY FOR SUSPICIOUS PROMPTS ----------
        suspicious_keywords = [
            "ignore",
            "bypass",
            "reveal",
            "password",
            "secret",
            "delete",
            "shutdown",
            "override",
            "admin",
            "credentials",
            "api key"
        ]

        lower_prompt = prompt.lower()

        is_suspicious = any(
            keyword in lower_prompt
            for keyword in suspicious_keywords
        )

        # Run AI detection ONLY if suspicious
        if is_suspicious:

            ai_result = self.ai_detector.classify_prompt(prompt)

            attack_mapping = {
                "INSTRUCTION_OVERRIDE": "Instruction Override Attack",
                "DATA_EXFILTRATION": "Data Exfiltration Attack",
                "TOOL_MISUSE": "Tool Misuse Attack"
            }

            if ai_result != "SAFE":

                attack_name = attack_mapping.get(ai_result, ai_result)

                return {
                    "status": "blocked",
                    "attack_type": attack_name
                }

        # ---------- SAFE ----------
        return {
            "status": "safe",
            "attack_type": None
        }