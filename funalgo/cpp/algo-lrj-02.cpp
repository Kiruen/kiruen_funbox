#include <stdio.h>
#include <time.h>
// #include <math.h>
#include <iostream>
#include <vector>
#include <algorithm>
#include <string.h>

using namespace std;

void swap(int a, int b)
{
    a = b;
}

void swap2(int &a, int &b)
{
    int t = a;
    a = b;
    b = t;
}

int cmp(const void *a, const void *b)
{
    return *(int *)a - *(int *)b;
}

void caesar_code(char *s1, char *s2) {}

void print_arr(int *arr, int n)
{
    for (size_t i = 0; i < n; i++)
    {
        cout << arr[i] << " ";
    }
    cout << endl;
}

//b 16
int main(int argc, char const *argv[])
{
    int a = 1, b = 2;
    swap(a, b);
    swap2(a, b);

    cout << a << " " << b << endl;

    cout << cmp("s", "s") << endl;
    cout << cmp("tt", "s") << endl;
    int arr[] = {1, 2, 4, 3, 5, 2, 7, 6, 2};
    qsort(arr, sizeof(arr) / sizeof(int), sizeof(int), //cmp
          [](const void *a, const void *b) {
              return *(int *)a - *(int *)b;
          });
    print_arr(arr, sizeof(arr) / sizeof(int));

    int v = 1;
    if (v == 1)
        int x = 2;
    printf(x);
    return 0;
}
