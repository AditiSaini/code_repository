from typing import List, Dict

"""
LeetCode Problem: Maximum Category Discount

Problem Description

You are working on an e-commerce platform that organizes products in a category hierarchy. Each product is tagged with a leaf-level category, and each category can optionally have a discount. A category can belong to multiple parent categories (i.e., the hierarchy can be a DAG rather than a strict tree).

The discount for a product is calculated as the maximum discount among all categories from the product’s category up to all possible root categories.

Write a function that, given:

A list of products with their leaf-level category.

A dictionary of category parent relationships (category → list of parents).

A dictionary of discounts for some categories.

Return the discount for each product.
"""

from collections import defaultdict, deque


class DiscountCalculator:
    def __init__(self, products: List[str], categories: Dict[str, List[str]], discounts: Dict[str, int]):
        self.products = products
        self.categories = categories
        self.discounts = discounts
        self.node_dependency = self.preprocess()
        
    def preprocess(self) -> Dict[str, int]:
        queue = deque()
        #Add product nodes in the graph 
        for p in self.products:
            _, category = p.split(':')
            self.categories[p] = [category]
        #Node dependency for products
        node_dependency = defaultdict(set)
        for p in self.products:
            queue = deque()
            queue.append(p)
            visited = set()
            while queue:
                node = queue.popleft()
                visited.add(node)
                for neigh in self.categories[node]:
                    if neigh not in visited:
                        queue.append(neigh)
            node_dependency[p] = visited
        return node_dependency
    
    def get_max_discounts(self) -> Dict[str, int]:
        #Calculate max discount
        max_discounts = defaultdict(int)
        for p in self.products:
            for node in self.node_dependency[p]:
                if node in self.discounts:
                    max_discounts[p] = max(max_discounts[p], self.discounts[node])
                else:
                    max_discounts[p] = max(max_discounts[p], 0)
        print(max_discounts)
        return max_discounts
    

# 🧪 TEST CASE 1 — Basic Case (From Problem Description)
products = [
    "Tea_Towels:C3_Tea_Towels",
    "Dinner_Towels:C3_Towels",
    "Coffee_Mugs:C3_Drinkware"
]
categories = {
    "C3_Tea_Towels": ["C2_Kitchen"],
    "C3_Towels": ["C2_Kitchen"],
    "C3_Drinkware": ["C2_Kitchen"],
    "C2_Kitchen": ["C1_Home", "C1_Gifts"],
    "C2_Living_Room": ["C1_Home"],
    "C1_Home": [],
    "C1_Gifts": []
}
discounts1 = {
    "C3_Towels": 5,
    "C2_Kitchen": 10,
    "C1_Home": 20
}
expected1 = {
    "Tea_Towels:C3_Tea_Towels": 20,
    "Dinner_Towels:C3_Towels": 20,
    "Coffee_Mugs:C3_Drinkware": 20
}
dc = DiscountCalculator(products, dict(categories), discounts1)    
assert dc.get_max_discounts() == expected1
print("✅ TEST CASE 1 PASSED — Basic DAG discount propagation")

# 🧪 TEST CASE 2 — Leaf node itself has highest discount
discounts2 = {
    "C3_Tea_Towels": 50,
    "C2_Kitchen": 10,
    "C1_Home": 20
}
expected2 = {
    "Tea_Towels:C3_Tea_Towels": 50,
    "Dinner_Towels:C3_Towels": 20,
    "Coffee_Mugs:C3_Drinkware": 20
}
dc = DiscountCalculator(products, dict(categories), discounts2)
assert dc.get_max_discounts() == expected2
print("✅ TEST CASE 2 PASSED — Leaf category dominates")

# 🧪 TEST CASE 3 — No discounts anywhere
discounts3 = {}
expected3 = {
    "Tea_Towels:C3_Tea_Towels": 0,
    "Dinner_Towels:C3_Towels": 0,
    "Coffee_Mugs:C3_Drinkware": 0
}
dc = DiscountCalculator(products, dict(categories), discounts3)
assert dc.get_max_discounts() == expected3
print("✅ TEST CASE 3 PASSED — No discounts available")

# 🧪 TEST CASE 4 — Category belongs to multiple parents (DAG)
categories2 = {
    "C3_Mugs": ["C2_Kitchen", "C2_Decor"],
    "C2_Kitchen": ["C1_Home"],
    "C2_Decor": ["C1_Gifts"],
    "C1_Home": [],
    "C1_Gifts": []
}
products2 = ["Coffee_Mug:C3_Mugs"]
discounts4 = {
    "C1_Home": 15,
    "C1_Gifts": 25,
    "C2_Decor": 10
}
expected4 = {"Coffee_Mug:C3_Mugs": 25}  # max path discount
dc1 = DiscountCalculator(products2, dict(categories2), discounts4)
assert dc1.get_max_discounts() == expected4
print("✅ TEST CASE 4 PASSED — Multi-parent propagation")

