from image_prcoesses import extract as extract_img_grid
from digit_Recognition_CNN import run as create_and_save_Model
from predict import extract_number_image as sudoku_extracted
from solve_v2 import solve_main, generate_clues,keyboard_input


def display_gameboard(sudoku):
    for i in range(len(sudoku)):
        if i % 3 == 0:
            if i == 0:
                print(" ┎─────────┰─────────┰─────────┒")
            else:
                print(" ┠─────────╂─────────╂─────────┨")

        for j in range(len(sudoku[0])):
            if j % 3 == 0:
                print(" ┃ ", end=" ")

            if j == 8:
                print(sudoku[i][j] if sudoku[i][j] != 0 else ".", " ┃")
            else:
                print(sudoku[i][j] if sudoku[i][j] != 0 else ".", end=" ")

    print(" ┖─────────┸─────────┸─────────┚")


# def main():
#     # Calling the image_prcoesses.py extract function to get a processed np.array of cells
#     image_grid = extract_img_grid()
#     print("Image Grid extracted")
#
#     # note we have alreday created and stored the model but if you want to do that again use the following command
#     # create_and_save_Model()
#
#     # Sudoku extract
#     sudoku = sudoku_extracted(image_grid)
#     print("Extracted and predict digits in the Sudoku")
#
# print("\n\nSudoku:")
# display_gameboard(sudoku)
#
#     # print(sudoku)
#     solve_main(sudoku)
#     display_gameboard(sudoku)
#     # print("\nSolving the Sudoku...\n")
#     # solvable, solved = solve_sudoku(sudoku)
#
#     # if(solvable):
#     #     print("\nSolved Sudoku:")
#     #     display_gameboard(solved)
#
#     print("Program End")


# if __name__ == '__main__':
#     main()

def main():
    print("Hi and welcome to  the Sudoku program made by Arjun.\n\nWhat would you like to do today?")
    user_input = input("Type S to solve or G to generate\n")
    while True:

        if user_input == "S":
            print("Would you like to use an image input or string input?")
            input_method = input("Enter I for image and S for string.\n")
            if input_method == "I":
                image_grid = extract_img_grid()
                print("Image Grid extracted")
                sudoku = sudoku_extracted(image_grid)
                print("Extracted and predict digits in the Sudoku")
            elif input_method == "S":
                sudoku = keyboard_input()

            print("\n\nSudoku:")
            display_gameboard(sudoku)
            solve_main(sudoku)
            display_gameboard(sudoku)
            print("Program End")

            if next_action():
                exit()
            else:
                main()

        elif user_input == "G":
            grid = generate_clues()
            display_gameboard(grid)

            if next_action():
                exit()
            else:
                main()

        elif user_input == "E":
            print("The program will exit now.")

            exit()

        else:
            print("Sorry I didn't get that. Please re-enter the letter corresponding to the function that you want.")
            user_input = input("Type S to solve or G to generate\n")


def next_action():
    print("Would you like to continue with the program?")
    user = input("Enter y/n\n")
    if user == "y":
        return False
    else:
        return True


main()
