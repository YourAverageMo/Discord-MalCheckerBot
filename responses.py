import random


def handle_response(user) -> str:
    """Main mal_check command logic.

    Args:
        user (str): provided by discord.Member.name

    Returns:
        str: evaluates the user name to determine if they they are mal or not uses if statments to set specific returns
    """
    user_lower = user.lower()

    if user_lower == "ibosh" or user_lower == "fluffyz":
        return f"Oh ya {user} is definitely a Mal, no question."
    if user_lower == "tdoubleyoua":
        return f"I am obligated at gunpoint to say, {user} is definitely not a Mal."

    else:
        ran = random.randint(0, 1)
        if ran == 0:
            return f"Nah {user} isnt a Mal"
        else:
            return f"Yup, {user} is a Mal"