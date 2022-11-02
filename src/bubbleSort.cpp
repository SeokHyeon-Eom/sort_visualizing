#include <iostream>
using namespace std;

void swap(int &a, int &b)
{
    int tmp = a;
    a = b;
    b = tmp;
}


void bubbleSort(int arr[], int start, int end)
{
    for(int i = 0; i < end - 1; i++)
    {
        for(int j = 1; j <= end - i; j++)
        if(arr[j] < arr[j - 1])
            swap(arr[j], arr[j - 1]);
    }
}

int main()
{
    int arr[10] = {4, 7, 9, 0, 1, 6, 2, 8, 3, 5};

    bubbleSort(arr, 0, 10);

    for(int i = 0; i < 10; i++)
        cout << arr[i] << " ";

    return 0;
}
