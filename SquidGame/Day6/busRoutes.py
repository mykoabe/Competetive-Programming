from collections import defaultdict, deque 
class Solution:
      def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0

        graph = defaultdict(set)  
        for i, stops in enumerate(routes):
            for stop in stops:
                graph[stop].add(i)  

        queue = deque([(source, 0)]) # (stop, num_changes)
        seen_stops = set([source])
        seen_routes = set()
        
        while queue:
            stop, num_changes = queue.popleft()
            if stop == target:
                return num_changes
            
            for i in graph[stop]:
                if i not in seen_routes:
                    seen_routes.add(i)
                    for stop in routes[i]:
                        if stop not in seen_stops:
                            seen_stops.add(stop)
                            queue.append((stop, num_changes + 1))
        
        return -1
                