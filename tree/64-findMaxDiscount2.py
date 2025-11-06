from typing import List, Dict
from collections import deque, defaultdict
"""
LeetCode Problem: Maximum Category Discount

Problem Description

You are working on an e-commerce platform that organizes products in a category hierarchy. Each product is tagged with a leaf-level category, and each category can optionally have a discount. A category can belong to multiple parent categories (i.e., the hierarchy can be a DAG rather than a strict tree).

The discount for a product is calculated as the maximum discount among all categories from the product’s category up to all possible root categories.

Write a function that, given:

A list of products with their leaf-level category.

A dictionary of category child relationships (category → list of child).

A dictionary of discounts for some categories.

Return the discount for each product.
"""

def find_max_discount(products: List[str], categories: Dict[str, List[str]], discounts: Dict[str, int]):
    """
    In this approach I will not do it with preprocessing but will try to calculate discounts for each node as we go
    """
    queue = deque()
    #Adds products to the graph 
    for p in products:
        _, category = p.split(':')
        if category in categories:
            categories[category].append(p)
        else:
            categories[category]=[p]
    max_discounts = defaultdict(int)
    #Adds parent node to the queue 
    for node in categories:
        if "C1" in node:
            max_discount = 0
            if node in discounts:
                max_discount = max(discounts[node], max_discount)
            max_discounts[node] = max_discount
            queue.append((node, max_discount))
    while queue:
        node, max_discount = queue.popleft()
        max_discounts[node] = max(max_discount, max_discounts[node])
        if node in categories:
            for neigh in categories[node]:
                if neigh in discounts:
                    max_discount = max(max_discount, discounts[neigh])
                queue.append((neigh, max_discount))
    final_discounts = {}
    for md in max_discounts:
        if md in products:
            final_discounts[md] = max_discounts[md]
    return final_discounts



categories = {
    "C1_Home": ["C2_Kitchen", "C2_Living_Room"],
    "C1_Gifts": ["C2_Kitchen"],
    "C2_Kitchen": ["C3_Tea_Towels", "C3_Towels", "C3_Drinkware"]
}

discounts = {
    "C3_Towels": 5,
    "C2_Kitchen": 10,
    "C1_Home": 20
}

products = [
    "Tea_Towels:C3_Tea_Towels",
    "Dinner_Towels:C3_Towels",
    "Coffee_Mugs:C3_Drinkware"
]

expected = {
    "Tea_Towels:C3_Tea_Towels": 20,
    "Dinner_Towels:C3_Towels": 20,
    "Coffee_Mugs:C3_Drinkware": 20
}

assert find_max_discount(products, categories, discounts)==expected
print("✅ TEST CASE 1 PASSED — Basic DAG discount propagation")