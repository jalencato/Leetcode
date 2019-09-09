// Problem 4.cpp : 此文件包含 "main" 函数。程序执行将在此处开始并结束。
//

//Finding the median of two sorted array
#include <iostream>
#include <vector>

using namespace std;

double max(double A, double B){
	return A > B ? A : B;
}

double min(double A, double B) {
	return A < B ? A : B;
}

double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
	int sizes1 = nums1.size();
	int sizes2 = nums2.size();
	if (sizes1 > sizes2) { // to ensure m<=n
		swap(nums1, nums2);
		swap(sizes1, sizes2);
	}

	//binary normalize the final result
	int iMin = 0, iMax = sizes1, target = (sizes1 + sizes2 + 1) / 2;
	while (iMin <= iMax) {
		int i = (iMin + iMax) / 2;
		int j = target - i;

		if (i < iMax && nums2[j - 1] > nums1[i]) 
			iMin = i + 1; // i is too small
		else if (i > iMin && nums1[i - 1] > nums2[j])
			iMax = i - 1; // i is too big
		else { // i is perfect
			int maxLeft;
			if (i == 0) maxLeft = nums2[j - 1]; 
			else if (j == 0) maxLeft = nums1[i - 1]; 
			else maxLeft = max(nums1[i - 1], nums2[j - 1]); 
			if ((sizes1 + sizes2) % 2 == 1) return maxLeft;

			int minRight;
			if (i == sizes1) minRight = nums2[j]; 
			else if (j == sizes2) minRight = nums1[i]; 
			else minRight = min(nums2[j], nums1[i]); 

			return (maxLeft + minRight) / 2.0;
		}
	}
	return 0.0;
}


int main(){
	vector<int> num1 = { 1,2 };
	vector<int> num2 = { 3,4 };
	auto res = findMedianSortedArrays(num1, num2);
	cout << res;
}