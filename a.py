def college_info_bot():
    print(" Welcome to the College Information Bot!")
    print("You can ask about: 'college name', 'courses', 'departments', 'principal',"
          "'HOD', 'events', or type 'exit' to quit.")
    
    while True:
        query = input("\nYou: ").lower()
        
        if "college name" in query:
            print("Bot: My college name is 'PVP College, Loni'.")
        elif "courses" in query:
            print("Bot: We offer B.Sc, BCA, M.Sc (Computer Science), and Ph.D. programs.")
        elif "departments" in query:
            print("Bot: The departments are Computer Science, Physics, Mathematics, and Electronics.")
        elif "principal" in query:
            print("Bot: The current principal is Dr. Pawar.")
        elif "hod" in query:
            print("Bot: The current HOD of Computer Science is Mrs. Galande.")
        elif "events" in query:
            print("Bot: The college organizes TechFest, Cultural Fest, and Sports Week every year.")
        elif "exit" in query or "bye" in query:
            print("Bot: Thank you for chatting! Have a great day.")
            break
        else:
            print("Bot: Sorry, I don’t have information about that. Please try another question.")

college_info_bot()
