
def moderate_feedback(feedback, target_words):
    feedback = feedback.strip()

    for word in target_words:
        feedback = feedback.replace(word, "*" * len(word))

    return feedback


feedback = input("Enter customer feedback: ")

target_words = ["bad", "hate", "angry", "sad"]

result = moderate_feedback(feedback, target_words)

print("\n--- Moderated Feedback ---")
print(result)