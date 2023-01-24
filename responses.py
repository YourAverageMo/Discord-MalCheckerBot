import random


def handle_response(user) -> str:
    user_lower = user.lower()
    
    if user_lower == "iBosh" or user_lower == "Fluffyz":
        return f"Oh ya {user} is definitely a Mal, no question."

    else:
        ran = random.randint(0,1)
        if ran == 0:
            return f"Nah {user} isnt a Mal"
        else:
            return f"Yup, {user} is a Mal"