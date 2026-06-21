print("================================")
print("     CHATBOT")
print("================================")
print("Type 'help' to see what you can ask, or 'bye' to exit.")

while True:
    question = input("\nAsk something about my Baba: ").lower()

    if "help" in question:
        print("You can ask about: name, job, education, farming, landlord, duty, guidance, personality, or goal.")

    elif "name" in question:
        print("My Baba's name is Muhammad Yousaf.")

    elif "job" in question or "work" in question:
        print("He is a hardworking farmer and a landlord.")

    elif "education" in question:
        print("He completed his FA and has since focused on managing the land and our family business.")

    elif "farming" in question or "landlord" in question:
        print("Being a landlord and a farmer is his life's work. He oversees the land and ensures everything is managed properly.")

    elif "duty" in question or "guide" in question:
        print("His daily duty involves hands-on farming work and guiding other employees to ensure the land is productive.")

    elif "personality" in question:
        print("He is a man of the soil—very grounded, honest, and hardworking. He leads by example.")

    # --- Additional Questions ---

    elif "routine" in question or "morning" in question:
        print("He is up before the sun! He likes to check the fields early in the morning when the air is fresh.")

    elif "leadership" in question:
        print("He believes in teaching, not just commanding. He guides his employees so they can learn how to do the work the right way.")

    elif "challenges" in question or "stress" in question:
        print("Farming has its challenges, like the weather, but he meets them with patience and faith.")

    elif "pride" in question:
        print("He is proud of the harvest and the fact that his hard work feeds so many people.")

    elif "future" in question:
        print("His future goal is to modernize the way we farm while keeping the values of honesty and hard work at the center.")

    elif "advice" in question:
        print("He often says, 'If you treat the land well, the land will treat you well.' It’s a lesson about respect and hard work.")

    elif "team" in question:
        print("He treats his employees with great fairness. He knows that his success depends on their effort too.")

    elif "home" in question:
        print("After a day in the fields, he values his peace at home more than anything.")

    elif "strength" in question:
        print("His physical and mental strength—he can work in the fields all day and still come home with a smile.")

    elif "bye" in question:
        print("Goodbye! Take care.")
        break

    else:
        print("I'm not sure about that. Try asking 'help' to see what you can ask me!")