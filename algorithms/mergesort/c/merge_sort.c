#include <stdio.h>

void merge_sort(int *arr, int a, int b);
void merge(int *arr1, int n1, int *arr2, int n2, int *mergedarr);

int main()
{
    int testarr[] = {6, 4, 8, 9, 3, 1, 2, 0};
    int t = (int)sizeof(testarr) / sizeof(testarr[0]);
    // int arr1[] = {4, 7, 9};
    // int arr2[] = {6, 7, 8};
    // int n1 = (int)sizeof(arr1) / sizeof(arr1[0]);
    // int n2 = (int)sizeof(arr2) / sizeof(arr2[0]);
    // int n3 = n1+ n2;
    // int arr3[n3];
    merge_sort(testarr, 0, t - 1);
    //	merge(arr1, n1, arr2, n2, arr3);

    int i;
    for (i = 0; i < t; i++)
    {
        printf("%d ", testarr[i]);
    }
    printf("\n");

    return 0;
}

void merge_sort(int *arr, int a, int b)
{
    if (a < b)
    {
        int m = a + (b - a) / 2;

        int n1 = m - a + 1;
        int n2 = b - m;
        int leftarr[n1];
        int rightarr[n2];
        int mergedarr[n1 + n2];
        int i, j;
        for (i = 0; i < n1; i++)
        {
            leftarr[i] = arr[a + i];
        }
        for (j = 0; j < n2; j++)
        {
            rightarr[j] = arr[m + 1 + j];
        }
        merge_sort(leftarr, a, m);
        merge_sort(rightarr, m + 1, b);

        merge(leftarr, n1, rightarr, n2, mergedarr);
    }
}

void merge(int *arr1, int n1, int *arr2, int n2, int *mergedarr)
{
    int i = 0, j = 0, k = 0;
    while (i < n1 && j < n2)
    {
        if (arr1[i] < arr2[j])
        {
            mergedarr[k] = arr1[i];
            i++;
        }
        else
        {
            mergedarr[k] = arr2[j];
            j++;
        }
        k++;
    }
    while (i < n1)
    {
        mergedarr[k] = arr1[i];
        i++;
        k++;
    }
    while (j < n2)
    {
        mergedarr[k] = arr2[j];
        j++, k++;
    }
}
