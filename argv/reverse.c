#include <stdio.h>
#include <cs50.h>
#include <string.h>

int main(void)
{
    string s = get_string("Type your name: ");
    printf("%s\n", s);

    int n=strlen(s);

    for(int i=0; i < n; i--)
    {
    printf("%c", s[i]);
    }
}