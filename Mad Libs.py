# Corrected implementation with regular expression re

import random
import os
import re

# Define the Mad Libs stories
stories = [
    "One day, [Name] decided to throw a surprise party for their [adjective] friend, [Friend’s Name]. They decorated the house with [color] balloons and a [adjective] banner. When [Friend’s Name] arrived, they were so [emotion] to see everyone. They spent the evening eating [food] and dancing to [music genre]. It was the best party ever!",
    
    "In the heart of a [adjective] jungle, explorer [Name] searched for hidden treasure. They followed a map marked with [adjective] symbols and crossed a [adjective] river. Finally, they found the treasure chest filled with [plural noun] and a [adjective] [noun]. [Name] couldn’t believe their luck!",
    
    "Wizard [Name] was brewing a magic potion in their [adjective] lab. They added [number] drops of [color] liquid, a pinch of [adjective] powder, and a [adjective] herb. The potion began to bubble and turned into a [adjective] color. When they drank it, they felt [emotion] and could speak to [animal]!",
    
    "While walking in the [adjective] forest, [Name] encountered a [adjective] creature with [number] legs and a [color] tail. The creature spoke in a [adjective] voice and offered [Name] a [adjective] [noun]. Surprised but intrigued, [Name] accepted the gift and continued their adventure.",
    
    "Brave [Name] set out on a quest to rescue the [adjective] [noun] trapped in a [adjective] tower. They fought off a [adjective] dragon and climbed a [adjective] ladder. Finally, they freed the [noun] and were hailed as a hero. The kingdom celebrated with a grand feast of [food] and [drink].",
    
    "One night, [Name] spotted a [color] spaceship landing in their [adjective] backyard. Out stepped a friendly alien with [number] eyes and a [color] antenna. The alien offered [Name] a [adjective] gift from their planet, which turned out to be a [noun] that could [verb] in incredible ways.",
    
    "On Halloween night, [Name] dared to enter the [adjective] haunted house at the end of the street. Inside, they encountered [number] [adjective] ghosts and a [color] cat that meowed in a spooky [adjective] tone. They were [emotion] but managed to find a [noun] that revealed the house’s secrets.",
    
    "During the school talent show, [Name] performed a [adjective] dance routine while wearing a [color] costume. Their friends cheered as they danced to [song] and performed tricks with a [noun]. The audience gave them a standing ovation, and [Name] felt [emotion] with joy.",
    
    "In the middle of winter, [Name] went on a [adjective] snow adventure. They built a [adjective] snowman with a [color] scarf and a [noun] hat. Afterward, they went ice skating on a [adjective] pond and enjoyed [food] by the campfire. It was a [adjective] day!",
    
    "[Name] wandered into a magical forest where every tree was [adjective] and the flowers smelled like [food]. They met a [adjective] unicorn who could [verb] and offered [Name] a [adjective] [noun]. With this magical gift, [Name] had an unforgettable day in the forest."
]

def get_input(prompt):
    return input(prompt + ": ")

def clear_screen():
    # Clear the screen based on device
    os.system('cls' if os.name == 'nt' else 'clear')

def extract_placeholders(story):
    # Use regex to find all placeholders in the form [placeholder]
    return set(re.findall(r'\[(.*?)\]', story))

def replace_placeholders(story, inputs):
    # Replace placeholders with user inputs
    def replace(match):
        placeholder = match.group(1)
        return inputs.get(placeholder, f"[{placeholder}]")

    # Use regex to replace placeholders in the story
    return re.sub(r'\[(.*?)\]', replace, story)

def main():
    # Randomly select a story
    story = random.choice(stories)

    # Extract placeholders from the story
    placeholders = extract_placeholders(story)

    # Create a dictionary to store user inputs
    inputs = {}

    # Ask for each placeholder value
    for placeholder in placeholders:
        inputs[placeholder] = get_input(f"Enter a {placeholder}")

    # Replace placeholders in the story with user inputs
    final_story = replace_placeholders(story, inputs)

    # Clear the screen and display the final story
    clear_screen()
    print(final_story)

if __name__ == "__main__":
    main()
# this implementation has an error might remove or fix this later correct implementation is listed above
# import random
# import os

# stories = [
#     "One day, [Name] decided to throw a surprise party for their [adjective] friend, [Friend’s Name]. They decorated the house with [color] balloons and a [adjective] banner. When [Friend’s Name] arrived, they were so [emotion] to see everyone. They spent the evening eating [food] and dancing to [music genre]. It was the best party ever!",
    
#     "In the heart of a [adjective] jungle, explorer [Name] searched for hidden treasure. They followed a map marked with [adjective] symbols and crossed a [adjective] river. Finally, they found the treasure chest filled with [plural noun] and a [adjective] [noun]. [Name] couldn’t believe their luck!",
    
#     "Wizard [Name] was brewing a magic potion in their [adjective] lab. They added [number] drops of [color] liquid, a pinch of [adjective] powder, and a [adjective] herb. The potion began to bubble and turned into a [adjective] color. When they drank it, they felt [emotion] and could speak to [animal]!",
    
#     "While walking in the [adjective] forest, [Name] encountered a [adjective] creature with [number] legs and a [color] tail. The creature spoke in a [adjective] voice and offered [Name] a [adjective] [noun]. Surprised but intrigued, [Name] accepted the gift and continued their adventure.",
    
#     "Brave [Name] set out on a quest to rescue the [adjective] [noun] trapped in a [adjective] tower. They fought off a [adjective] dragon and climbed a [adjective] ladder. Finally, they freed the [noun] and were hailed as a hero. The kingdom celebrated with a grand feast of [food] and [drink].",
    
#     "One night, [Name] spotted a [color] spaceship landing in their [adjective] backyard. Out stepped a friendly alien with [number] eyes and a [color] antenna. The alien offered [Name] a [adjective] gift from their planet, which turned out to be a [noun] that could [verb] in incredible ways.",
    
#     "On Halloween night, [Name] dared to enter the [adjective] haunted house at the end of the street. Inside, they encountered [number] [adjective] ghosts and a [color] cat that meowed in a spooky [adjective] tone. They were [emotion] but managed to find a [noun] that revealed the house’s secrets.",
    
#     "During the school talent show, [Name] performed a [adjective] dance routine while wearing a [color] costume. Their friends cheered as they danced to [song] and performed tricks with a [noun]. The audience gave them a standing ovation, and [Name] felt [emotion] with joy.",
    
#     "In the middle of winter, [Name] went on a [adjective] snow adventure. They built a [adjective] snowman with a [color] scarf and a [noun] hat. Afterward, they went ice skating on a [adjective] pond and enjoyed [food] by the campfire. It was a [adjective] day!",
    
#     "[Name] wandered into a magical forest where every tree was [adjective] and the flowers smelled like [food]. They met a [adjective] unicorn who could [verb] and offered [Name] a [adjective] [noun]. With this magical gift, [Name] had an unforgettable day in the forest."
# ]

# def get_input(prompt):
#     return input(prompt + ": ")

# def clear_screen():
#     # Clear the screen based on system
#     os.system('cls' if os.name == 'nt' else 'clear')

# def main():

#     # Randomly select a story
#     story = random.choice(stories)

#     # Extract placeholders from the story
#     # Define a set and slit story to each word and check if word contains bracket on start and end
#     placeholders = set()
#     for word in story.split():
#         if word.startswith('[') and word.endswith((']', '].', '],')): # I was damn tired so I didn't minded changing the code to fix this bug to detect letters so this was my lazy approach :D
#             placeholders.add(word[1:-1])

#     # Dictionary to store Use inputs for extracted words/Placeholders
#     inputs = {}

#     # Ask for each placeholder value
#     for placeholder in placeholders:
#         inputs[placeholder] = get_input(f"Enter a {placeholder}")

#     # Replacing placeholders in the story with user inputs
#     final_story = story
#     for placeholder, user_input in inputs.items():
#         final_story = final_story.replace(f"[{placeholder}]", user_input)

#     # ready for final story
#     clear_screen()
#     print(final_story)

# if __name__ == "__main__":
#     main()

