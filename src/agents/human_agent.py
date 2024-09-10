class HumanInputAgent:
    def run(self, diagnose_state: dict):
        print(diagnose_state)

        response = input("Please enter your response: ")
        return {"human_response": response}
