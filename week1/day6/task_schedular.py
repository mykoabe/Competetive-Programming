from collections import Counter
from typing import list
class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        
        count = Counter(tasks)
        
        largest_count = count[count.most_common()[0][0]]
        
        num_largest_groups = len([t for t, count in count.items() if count == largest_count])
        
        # Arrange the largest in the format of A _ _ A _ _ A. (Here A is largest with 3 elements and n = 2)
        slots_in_between = (largest_count - 1) * n  # num of partitions x size of each partition
        
        remaining_elements = len(tasks) - largest_count
        
        # We reduce the count of all other "largest groups" by one and will handle them later. Essentially,
        # they are to be appended to the back.
        remaining_elements -= num_largest_groups - 1
        
        # Slot all the elements in the partitions
        slots_in_between -= remaining_elements

        # If more slots are needed than we have, we can expand each partition to be bigger. So, we can ignore that
        slots_in_between = max(slots_in_between, 0)

        if slots_in_between > 0:
            return len(tasks) + slots_in_between
        
        return len(tasks)