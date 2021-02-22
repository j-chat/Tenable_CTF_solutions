#include <iostream>
#include <algorithm>

using namespace std;

void PrintNLowestNumbers(int arr[], unsigned int length, unsigned short nLowest)
{
 // print the n lowest numbers to stdout seperated by space character, do not de-dupe

  sort(arr, arr + length);
  for (int i = 0; i < nLowest; ++i)
    cout << arr[i] << " ";
}

int main()
{
	char input[0x100];
	int integerList[0x100];
	unsigned int length;
	unsigned short nLowest;
	std::cin >> nLowest;
	std::cin >> length;
	for (int i=0;i<length;i++)
		 std::cin >> integerList[i];
	PrintNLowestNumbers(integerList, length, nLowest);
    return 0; 
}
