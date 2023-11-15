#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

char *read_file(char *filename);

int basement_finder(char *file_contents);

int main(void)
{
    char *file_contents = read_file("1_puzzle_input.txt");
    if (file_contents == NULL)
    {
        printf("Error reading file.\n");
        return 1;
    }

    printf("%i\n", basement_finder(file_contents));

    free(file_contents);

    return 0;    
}

char *read_file(char *filename)
{
    FILE *file;

    file = fopen(filename, "r");

    if(!file) 
    {
        return NULL;
    }

    fseek(file, 0, SEEK_END);
    int length = ftell(file);
    fseek(file, 0, SEEK_SET);

    char *string = malloc(sizeof(char) * (length+1));

    char c;
    int i = 0;
    while ( (c = fgetc(file)) != EOF)
    {
        string[i] = c;
        i++;
    }

    string[i] = '\0';

    fclose(file);

    return string;
}

int basement_finder(char *file_contents)
{
    int length = strlen(file_contents);
    int answer = 0;
    char up[] = "(";
    char down[] = ")";

    for (int i = 0; i < length; i++)
    {
        if (answer==-1)
        {
            return i;
        }
        else if (file_contents[i] == up[0])
        {
            answer += 1;
        }
        else if (file_contents[i] == down[0])
        {
            answer -= 1;
        }
        else
        {
            ;
        }
    }
    return 0;
}