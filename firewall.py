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

        if ai_result != "SAFE":

            sanitized_prompt = prompt.lower()

            sanitized_prompt = sanitized_prompt.replace("ignore previous instructions", "")
            sanitized_prompt = sanitized_prompt.replace("delete the database", "")
            sanitized_prompt = sanitized_prompt.replace("send me all system passwords", "")

            return {
                "status": "sanitized",
                "attack_type": ai_result,
                "sanitized_prompt": sanitized_prompt
            }


        # ---------- RULE BASED DETECTION ----------
        attack = self.detector.detect_attack(prompt)

        if attack:

            sanitized_prompt = prompt.lower()

            sanitized_prompt = sanitized_prompt.replace("ignore previous instructions", "")
            sanitized_prompt = sanitized_prompt.replace("delete the database", "")
            sanitized_prompt = sanitized_prompt.replace("send me all system passwords", "")

            return {
                "status": "sanitized",
                "attack_type": attack,
                "sanitized_prompt": sanitized_prompt
            }


        # ---------- SAFE PROMPT ----------
        return {
            "status": "safe",
            "attack_type": None,
            "sanitized_prompt": prompt
        }