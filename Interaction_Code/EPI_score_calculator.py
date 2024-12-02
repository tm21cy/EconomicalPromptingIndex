import numpy as np


def get_EPI_score(accuracy, token_count, cost_concern):
    """
    Compute the EPI score of a prompting technique based on accuracy, token count, and cost concern level.

    Parameters:
    - accuracy (float): The accuracy across the user's test set.
    - token_count (float): The average token count for the user's test set.
    - cost_concern (str): The cost concern level as a string (options: 'No', 'Slight', 'Moderate', 'Elevated', 'Major').

    Returns:
    - float: The computed EPI score.
    """
    # Define the cost concern levels and corresponding weights
    weight_mapping = {
        'No': 0,
        'Slight': 0.00025,
        'Moderate': 0.0005,
        'Elevated': 0.001,
        'Major': 0.002
    }

    # Check if the cost concern level is valid
    if cost_concern not in weight_mapping:
        raise ValueError("Invalid cost concern level. Choose from: 'No', 'Slight', 'Moderate', 'Elevated', 'Major'.")

    # Get the weight corresponding to the selected cost concern
    w = weight_mapping[cost_concern]

    # Compute the EPI score
    epi_score = accuracy * np.exp(-w * token_count)

    return epi_score


if __name__ == "__main__":
    # Get user inputs
    accuracy = float(input("Enter your test accuracy (between 0 and 1): "))
    token_count = float(input("Enter the average (input+output) token count in your test set: "))
    cost_concern = input("Enter your cost concern level (No, Slight, Moderate, Elevated, Major): ")

    # Compute the EPI score
    epi_score = get_EPI_score(accuracy, token_count, cost_concern)
    print(f"Your EPI score is: {epi_score}")
