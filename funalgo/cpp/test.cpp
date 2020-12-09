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


int main(int argc, char const *argv[])
{

    // int v = 1;
    // if (v == 1)
    //     int x = 2;
    // printf(x);

    int *arr_of_point[12];  //由于[]的右结合性，[]先和p接触，arrof首先会被认为是个数组
    int *(arr_of_point2[12]);
    int (*arr_of_point3[12]);
    int (*arr_of_point3[12]);
    int (*point_of_arr)[12];  //p先和*接触，首先会被认为是个指针

    arr_of_point[0] = new int(100);
    // *arr_of_point = new int[12];
    *arr_of_point2 = *arr_of_point3 = new int[12];
    int arr[12] = {0};
    point_of_arr = &arr;
    // arr_of_point = &arr;

    cout << "值：" << *arr_of_point[0] << endl;

    // int arr_of_arr[][12] = {{0, 0}};
    // int (*poaa)[][12] = &arr_of_arr;
    int arr_of_arr[2][12] = {{0, 0}};
    int (*poaa)[2][12] = &arr_of_arr;

    int *arr = arr_of_arr[1];
    // int arr1[] = arr_of_arr[1];

    return 0;
}
