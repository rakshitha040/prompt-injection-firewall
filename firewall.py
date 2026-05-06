from detector import PromptDetector
from ai_detector import AIDetector


class PromptFirewall:

    def __init__(self):

        # Rule-based detector
        self.detector = PromptDetector()

        # AI-based detector
        self.ai_detector = AIDetector()

    def inspect_prompt(self, prompt):

        # ---------- AI BASED DETECTION ----------
        ai_result = self.ai_detector.classify_prompt(prompt)

        # Convert AI labels into readable attack names
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

        # ---------- RULE BASED DETECTION ----------
        attack = self.detector.detect_attack(prompt)

        if attack:

            return {
                "status": "blocked",
                "attack_type": attack
            }

        # ---------- SAFE PROMPT ----------
        return {
            "status": "safe",
            "attack_type": None
        }