#include <regex.h>
#include <stdio.h>
#include <string.h>
#include <sys/wait.h>
#include <unistd.h>

/*
Take User input and Pass it through a bash shell

NOTES:

  - We need to fork a process otherwise, the Exec command replaces our current
one
  - EXECV (path, [array])  Where Path is path to thing we want to run
  - Array is:
    - [0] bash  (Thing to run, could also be /bin/bash)
    - [1] "-c" Take input from a string as options
    - [2] input,  User input
    - [3] NULL : EOF

This Should be Enough here....

  https://www.shellscript.sh/quickref.html
*/

int main(void) {
  printf("Custom Shell Started\n");

  char input[100]; // Input Buffer
  int running = 1;
  int status = 0;
  ; // Status of our child
  char *arr[] = {"bash", "-c", NULL, NULL};
  regex_t regexp; // Regexp Filter
  int re;         // Compilation Result

  // Take pity on them and allow echo
  //  Also Fuck Negative Lookahead in Regexp to hell and back.
  re = regcomp(&regexp, "[^${}!#()<'\\,[:digit:]]", REG_EXTENDED);

  // Now we want this in a loop
  while (running == 1) {
    printf("> ");
    fflush(stdout);
    // scanf("%s", input);
    fgets(input, 100, stdin);

    // Strip any newlines (either \r\n or \n
    input[strcspn(input, "\r\n")] = 0;

    // printf("\nYou entered: >%s<\n", input);

    if (strcmp(input, "quit") == 0) {
      printf("Exit Called\n");
      return 1;
    } else if (strcmp(input, "exit") == 0) {
      printf("Exit Called\n");
      return 1;
    } else if (strcmp(input, "help") == 0) {
      printf("Sources on the challenge Page \nAlso "
             "https://www.shellscript.sh/quickref.html \n");
    }

    // Now scan it with the regexp
    int regexpResult = regexec(&regexp, input, 0, NULL, 0);
    if (regexpResult == REG_NOMATCH) {

      // We Process the thing

      // Fork a process
      pid_t pid = fork();
      if (pid < 0) {
        perror("Forking Error!!!\n");
      } else if (pid == 0) {
        // We are in the Child, so run our script
        fclose(stdin);
        arr[2] = input;
        for (int j = 0; j < 4; j++) {
          printf("%s\n", arr[j]);
        }
        execv("/bin/bash", arr);
      } else {
        wait(&status); // Wait for the process to finish
        printf("Command has Exited, Exit code was %d\n", status);
      }

    } else {
      printf("----- INVALID CHARACTER DETECTED -------\n");
    }
  }
}
