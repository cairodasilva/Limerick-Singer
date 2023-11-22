from genetic import genetic
import os

def recite():
    runner = genetic(0) 
    filename = input("Write the file name of a poem you want to reperform \
    (e.g., poem_20231121_000738.txt) ")
    file_path = os.path.join("./previous_poems", filename)
    if os.path.exists(file_path):
        runner.reperform_poem(filename)
    else:
        print(f"The file {filename} does not exist.")

def generate():
    generations = int(input(
    "How many generations would you like to run this algorithm for? "))
    name = str(input(
    "What song do you want to base your poem off of? "))
    artist = str(input(
    "Which artist is that song made by?"))
    runner = genetic(generations,name,artist)   
    runner.create_poems()
    runner.genetic_algo_runner()
    poem = runner.get_fittest()
    command = input("type 'yes' to say the poem just generated ")
    if command == "yes":
        runner.say(poem)


def main():
    choice = input("Do you want to generate a new poem to \
    reperform an old one?" + '\n' + "Type 'create' or 'recite'  ")
    if choice == "create":
        generate()
    if choice == "recite":
        recite()


if __name__ == "__main__":
    main()