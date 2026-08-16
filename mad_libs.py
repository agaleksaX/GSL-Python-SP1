import random


def choose_template():
    """Ask the user to choose a story template."""
    while True:
        print("\nChoose a story template:")
        print("1. A hospital visit")
        print("2. A camping trip")
        print("3. An enchanted castle")
        print("4. Choose a random template")

        choice = input("Enter 1, 2, 3, or 4: ")

        if choice == "1" or choice == "2" or choice == "3":
            return choice

        if choice == "4":
            choice = random.choice(["1", "2", "3"])
            print("Random template selected:", choice)
            return choice

        print("Invalid choice. Please enter a number from 1 to 4.")


def collect_words(prompts):
    """Collect one non-empty answer for every prompt."""
    answers = []

    for prompt in prompts:
        answer = input(prompt)

        while answer == "":
            print("The answer cannot be empty.")
            answer = input(prompt)

        answers.append(answer)

    return answers


def create_hospital_story():
    """Collect words and create the hospital story."""
    prompts = [
        "Type a number: ",
        "Type a measure of time: ",
        "Type a mode of transportation: ",
        "Type an adjective: ",
        "Type another adjective: ",
        "Type a noun: ",
        "Type a color: ",
        "Type a part of the body: ",
        "Type a verb: ",
        "Type another number: ",
        "Type another noun: ",
        "Type a third noun: ",
        "Type another part of the body: ",
        "Type a fourth noun: ",
        "Type one more adjective: ",
        "Type a silly word: ",
    ]
    words = collect_words(prompts)

    story = (
        f"It was about {words[0]} {words[1]} ago when I arrived at the "
        f"hospital in a {words[2]}. The hospital is a/an {words[3]} place, "
        f"there are a lot of {words[4]} {words[5]} here. There are nurses "
        f"here who have {words[6]} {words[7]}. If someone wants to come into "
        f"my room, I told them that they have to {words[8]} first. I've "
        f"decorated my room with {words[9]} {words[10]}. Today I talked to a "
        f"doctor and they were wearing a {words[11]} on their {words[12]}. "
        f"I heard that all doctors {words[8]} {words[13]} every day for "
        f"breakfast. The most {words[14]} thing about being in the hospital "
        f"is the {words[15]} {words[5]}!"
    )

    return story


def create_camping_story():
    """Collect words and create the camping story."""
    prompts = [
        "Type a person's name: ",
        "Type a noun: ",
        "Type an adjective describing a feeling: ",
        "Type a verb: ",
        "Type another adjective describing a feeling: ",
        "Type an animal: ",
        "Type another verb: ",
        "Type a color: ",
        "Type a verb ending in -ing: ",
        "Type an adverb ending in -ly: ",
        "Type a number: ",
        "Type a measure of time: ",
        "Type a silly word: ",
        "Type another noun: ",
    ]
    words = collect_words(prompts)

    story = (
        f"This weekend I am going camping with {words[0]}. I packed my "
        f"lantern, sleeping bag, and {words[1]}. I am so {words[2]} to "
        f"{words[3]} in a tent. I am {words[4]} we might see a(n) {words[5]}, "
        f"I hear they're kind of dangerous. While we're camping, we are "
        f"going to hike, fish, and {words[6]}. I have heard that the "
        f"{words[7]} lake is great for {words[8]}. Then we will {words[9]} "
        f"hike through the forest for {words[10]} {words[11]}. If I see a "
        f"{words[7]} {words[5]} while hiking, I am going to bring it home "
        f"as a pet! At night we will tell {words[10]} {words[12]} stories "
        f"and roast {words[13]} around the campfire!!"
    )

    return story


def create_castle_story():
    """Collect words and create the enchanted castle story."""
    prompts = [
        "Type a person's name: ",
        "Type an adjective: ",
        "Type a color: ",
        "Type an animal: ",
        "Type a place: ",
        "Type another adjective: ",
        "Type a plural magical creature: ",
        "Type a third adjective: ",
        "Type another plural magical creature: ",
        "Type a room in a house: ",
        "Type a noun: ",
        "Type another noun: ",
        "Type a plural noun: ",
        "Type a fourth adjective: ",
        "Type another plural noun: ",
        "Type a number: ",
        "Type a measure of time: ",
        "Type a verb ending in -ing: ",
        "Type a fifth adjective: ",
        "Type one more noun: ",
    ]
    words = collect_words(prompts)

    story = (
        f"Dear {words[0]}, I am writing to you from a {words[1]} castle in "
        f"an enchanted forest. I found myself here one day after going for "
        f"a ride on a {words[2]} {words[3]} in {words[4]}. There are "
        f"{words[5]} {words[6]} and {words[7]} {words[8]} here! In the "
        f"{words[9]} there is a pool full of {words[10]}. I fall asleep each "
        f"night on a {words[11]} of {words[12]} and dream of {words[13]} "
        f"{words[14]}. It feels as though I have lived here for {words[15]} "
        f"{words[16]}. I hope one day you can visit, although the only way "
        f"to get here now is {words[17]} on a {words[18]} {words[19]}!!"
    )

    return story


def main():
    """Run the Mad Libs game."""
    print("Welcome to Mad Libs!")
    template = choose_template()

    print("\nEnter words without seeing the story:")

    if template == "1":
        story = create_hospital_story()
    elif template == "2":
        story = create_camping_story()
    else:
        story = create_castle_story()

    print("\nYour Mad Libs story:\n")
    print(story)


main()