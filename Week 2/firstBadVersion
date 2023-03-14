# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

def firstBadVersion(n: int) -> int:
        left = 1
        right = n
        while (left < right):
            mid = int((left + right) / 2)
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
            
        return left

def main():
    print(firstBadVersion(5))

main()
