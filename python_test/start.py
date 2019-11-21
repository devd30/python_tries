#a=[2, 7, 11, 15]
#a=[3,2,4]
#target=9
#target=6
#pair=[]
'''for val in a:
    print val
    rem=val -target
    if rem in a:
       re=[rem[]]
       pair.extend(rem,val) 
'''
'''
for i in range(len(a)):
    rem= target - a[i]
    #print rem
    if (rem in a) and (rem + a[i] == target) and (i != a.index(rem)):
        print [i,a.index(rem)]
        break
    #print (i,a.index(rem))
'''
'''
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            rem= target - nums[i]
            #print rem
            if (rem in nums) and (rem + nums[i] == target) and (i != nums.index(rem)):
                return [i,nums.index(rem)]
'''


a=input()
b=input()
req=[]
increment = 0
for val in range(len(a)):
    #print val
    for j in range(len(b)):
        if val == j :
            output=a[val]+b[j] + increment
            #req.append(output)
            #print output
            if output > 9 :
                first=output//10
                second=output%10
                increment = first
                print increment
                req.append(second)
            else:
                req.append(output)
print req
