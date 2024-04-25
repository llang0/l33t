# 27. Remove Element

def removeElement( nums, val):
        dict = {}
        for i in range(len(nums)):
            if nums[i] in dict:
                dict[nums[i]].append(i)
            else: 
                dict[nums[i]] = [i]

        if not val in dict:
            return len(nums)

        indicies = dict[val]
        l = len(indicies)

        for _ in range(len(indicies)):
            index = indicies.pop()
            nums.pop(index)

        del dict[val]

        return len(nums)