class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # M1 (refer M2 much optimised and ez) 
        # left=right=0
        # temp=[]
        # while (left<m and right<n):
        #     if nums1[left]<=nums2[right]:
        #         temp.append(nums1[left])
        #         left+=1
        #     else:
        #         temp.append(nums2[right])
        #         right+=1
        # #any one of the array might b exhausted and exited 
        # while left<m:
        #     temp.append(nums1[left])
        #     left+=1
        # while right<n:
        #     temp.append(nums2[right])
        #     right+=1
        # # print(temp)
        # # nums1=temp - this wont work -as this only changes the local ref 
        # for i in range(len(temp)):
        #     nums1[i]=temp[i]


        #NOTE: .sort() N*logN => in py uses (modified mergesort and quicksort - both of TC N*logN)
        #M2 - https://leetcode.com/problems/merge-sorted-array/solutions/29503/beautiful-python-solution/comments/763188 

        while (m>0 and n>0): #no need fot m>0 contd 
            if nums1[m-1]>=nums2[n-1]:
                nums1[m+n-1]=nums1[m-1]
                m-=1
            else:
                nums1[m+n-1]=nums2[n-1]
                n-=1
        #if nums2 exhausted (as here nums1 cant exhaust bfore nums1)
        if n>0:
            nums1[:n]=nums2[:n]

