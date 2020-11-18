#include <stdio.h>
#include <time.h>
// #include <math.h>
#include <iostream>
#include <vector>
#include <algorithm>
#include <string.h>

using namespace std;
void factorial_sum()
{
    const int MOD = 1000000;

    int n, S = 0;
    scanf("%d", &n);

    for (int i = 1; i <= n; i++)
    {
        int factorial = 1;
        for (int j = 1; j <= i; j++)

            factorial = (factorial * j % MOD);
        S = (S + factorial) % MOD;
    }

    printf("%d\n", S);

    printf("Time used = %.2f\n", (double)clock() / CLOCKS_PER_SEC);
}

void permutation()
{
    for (size_t i = 0; i < 9; i++)
    {
        for (size_t j = 0; j != i && j < 9; j++)
        {
            for (size_t k = 0; k != i && k != j && k < 9; k++)
            {
                int abc = i * 100 + j * 10 + k;
                int def = abc * 2;
                int ghi = abc * 3;
                //想要所有数字都不重复，可以def ghi的各个数字逐个判断，挺无聊的
                printf("%d %d %d\n", abc, def, ghi);
            }
        }
    }
}

int *light_switch(int n, int k)
{
    int *switches = new int[n]{0};
    for (size_t i = 1; i <= k; i++)
    {
        for (size_t j = 1; j <= n; j++)
        {
            if (j % i == 0)
                switches[j - 1] = !switches[j - 1];
        }
    }
    for (size_t i = 0; i < n; i++)
    {
        printf("%d", switches[i]);
    }

    return switches;
}

void check_if_valid_vertical(char *char_set)
{
    int count = 0;
    char temp[100];
    for (size_t abc = 111; abc < 999; abc++)
    {
        for (size_t de = 11; de < 99; de++)
        {
            int lv1 = abc * (de % 10), lv2 = abc * (de / 10), res = abc * de;
            sprintf(temp, "%d%d%d%d%d", abc, de, lv1, lv2, res);
            bool ok = true;
            for (size_t k = 0; k < strlen(temp); k++)
            {
                if (strchr(char_set, temp[k]) == NULL)
                    ok = false;
            }
            if (ok)
            {
                printf("<%d>\n", ++count);
                printf("%5d\nX%4d\n-----\n%5d\n%4d\n-----\n%5d\n\n", abc, de, lv1, lv2, res);
            }
        }
    }
}



// echo 20 | .\algo1.exe
//  g++ .\algo-lrj-01.cpp -Wall -o algo1.exe
int main(int argc, char const *argv[])
{
    // factorial_sum();
    // permutation();
    // light_switch(7, 3);
    check_if_valid_vertical("23578");
    return 0;
}
