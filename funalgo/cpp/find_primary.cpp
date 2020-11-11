#include <iostream>

using namespace std;
int max(int a[], int len)
{
    int max = -1;
    for (size_t i = 0; i < len; i++)
    {
        if (a[i] > max)
            max = a[i];
    }
    return max;
}

int find_primary1(int a[], int len)
{
    int max_size = max(a, len);
    int *counts = new int[max_size] { 0};
    for (size_t i = 0; i < len; i++)
    {
        counts[a[i]]++;
    }
    for (size_t i = 0; i < max_size; i++)
    {
        if (counts[i] > len / 2)
            return i;
    }
    // delete counts;
    return -1;
}

int find_primary2(int arr[], int len)
{
    int primary = arr[0];
    int state = 1;
    for (size_t i = 1; i < len; i++)
    {
        if (arr[i] != primary)
        {
            state--;
        }
        else
        {
            state++;
        }
        if (state < 0 && arr[i] != primary)
        {
            primary = arr[i];
        }
    }
    return state > 0 ? primary : -1;
}

int main(int argc, char const *argv[])
{
    int arr1[] = {1, 1, 1, 2, 3, 4, 4, 1, 4, 4, 1, 1, 1};
    cout << find_primary1(arr1, sizeof(arr1) / sizeof(int)) << endl;
    int arr2[] = {1, 1, 1, 4, 1, 3, 1, 4, 1, 4, 1, 4, 4, 4, 1, 4, 1, 1, 1};
    cout << find_primary2(arr2, sizeof(arr2) / sizeof(int)) << endl;
    return 0;
}
