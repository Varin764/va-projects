#include <stdio.h>

void startGame() {
    int choice1, choice2, choice3;

    printf("Welcome to Blood Miridian!\n");
    printf("You wake up at the edge of a dark forest. What do you do?\n");
    printf("1. Enter the forest\n");
    printf("2. Walk along its edge\n");
    printf("Enter your choice (1 or 2): ");
    scanf("%d", &choice1);

    if (choice1 == 1) {
        printf("\nYou bravely enter the forest.\n");
        printf("After walking for a while, you see a fork in the path.\n");
        printf("1. Take the left path\n");
        printf("2. Take the right path\n");
        printf("Enter your choice (1 or 2): ");
        scanf("%d", &choice2);

        if (choice2 == 1) {
            printf("\nThe left path leads you to the church.\n");
            printf("Do you want to:\n");
            printf("1. Enter the church\n");
            printf("2. Turn back\n");
            printf("Enter your choice (1 or 2): ");
            scanf("%d", &choice3);

            if (choice3 == 1) {
                printf("\nThe chruch is empty...\n");
                printf("Congratulations! You win!\n");
            } else {
                printf("\nYou find him standing ahead, The Blood Meridian is over as a new age comes in humanity.\n");
                printf("Game Over.\n");
            }
        } else {
            printf("\nThe right path leads you to a river.\n");
            printf("You try to cross, but the current is too strong.\n");
            printf("You are swept away.\n");
            printf("Game Over.\n");
        }
    } else if (choice1 == 2) {
        printf("\nYou decide to walk along the forest edge.\n");
        printf("You find a small village.\n");
        printf("Do you:\n");
        printf("1. Enter the village\n");
        printf("2. Keep walking\n");
        printf("Enter your choice (1 or 2): ");
        scanf("%d", &choice2);

        if (choice2 == 1) {
            printf("\nThe villagers welcome you.\n");
            printf("You live happily in the village.\n");
            printf("Happy Ending!\n");
        } else {
            printf("\nYou keep walking and you find him standing ahead, The Blood Meridian is over as a new age comes in humanity.\n");
            printf("There's nowhere else to go.\n");
            printf("Game Over.\n");
        }
    } else {
        printf("\nInvalid choice. Game Over.\n");
    }
}

int main() {
    char playAgain;
    do {
        startGame();
        printf("\nDo you want to play again? (y/n): ");
        scanf(" %c", &playAgain);
    } while (playAgain == 'y' || playAgain == 'Y');

    printf("Thank you for playing The Blood Meridian!\n");
    return 0;
}
