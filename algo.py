import tkinter as tk
from tkinter import ttk

# Fonction pour mettre à jour la liste d'algorithmes en fonction de la recherche
def mettre_a_jour_liste(event):
    recherche = recherche_entree.get().lower()  # Obtient la recherche en minuscules
    algo_liste.delete(0, tk.END)  # Efface la liste actuelle
    for algo in algorithmes:
        if recherche in algo.lower():  # Vérifie si la recherche est dans le nom de l'algorithme
            algo_liste.insert(tk.END, algo)

# Fonction pour afficher les détails d'un algorithme sélectionné
def afficher_details(event):
    selected_item = algo_liste.get(algo_liste.curselection())  # Obtient l'élément sélectionné
    details_text.delete(1.0, tk.END)  # Efface le texte précédent
    if selected_item:
        details_text.insert(tk.END, descriptions[selected_item])

# Crée une fenêtre principale
fenetre = tk.Tk()
fenetre.title("Bibliothèque d'Algorithmes Mathématiques")

# Crée une liste d'algorithmes et leurs descriptions correspondantes
algorithmes = ["Bubble Sort",
    "Quick Sort",
    "Merge Sort",
    "Binary Search",
    "Depth-First Search (DFS)",
    "Breadth-First Search (BFS)",
    "Dijkstra's Algorithm",
    "Fibonacci (Recursive)",
    "Fibonacci (Dynamic Programming)",
    "Knapsack (Dynamic Programming)"]
descriptions = {
     "Bubble Sort": """
def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    """,

    "Quick Sort": """
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)
    """,

    "Merge Sort": """
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result
    """,

    "Binary Search": """
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1  # Target not found
    """,

    "Depth-First Search (DFS)": """
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for neighbor in graph[start] - visited:
        dfs(graph, neighbor, visited)
    """,

    "Breadth-First Search (BFS)": """
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)
    """,

    "Dijkstra's Algorithm": """
import heapq

def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    """,

    "Fibonacci (Recursive)": """
def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)
    """,

    "Fibonacci (Dynamic Programming)": """
def fibonacci_dp(n):
    fib = [0] * (n + 1)
    fib[1] = 1

    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]

    return fib[n]
    """,

    "Knapsack (Dynamic Programming)": """
def knapsack(weights, values, capacity):
    n = len(weights)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]
    """
}

# Crée une barre de recherche avec un placeholder
recherche_entree = ttk.Entry(fenetre)
recherche_entree.insert(0, "Search")  # Ajoute le placeholder
recherche_entree.grid(row=0, column=0, columnspan=2, sticky="ew")  # Utilisation de grid

# Supprimer le placeholder lorsque l'utilisateur clique sur la barre de recherche
def supprimer_placeholder(event):
    if recherche_entree.get() == "Search":
        recherche_entree.delete(0, tk.END)

recherche_entree.bind("<FocusIn>", supprimer_placeholder)

# Crée un panneau pour afficher les détails
details_text = tk.Text(fenetre, wrap=tk.WORD, width=40, height=10)
details_text.grid(row=1, column=1, sticky="nsew")  # Utilisation de grid, sticky="nsew" pour remplir verticalement

# Crée une liste déroulante pour afficher les algorithmes
algo_liste = tk.Listbox(fenetre)
for algo in algorithmes:
    algo_liste.insert(tk.END, algo)
algo_liste.grid(row=1, column=0, sticky="ns")  # Utilisation de grid, sticky="ns" pour remplir verticalement

# Configure la répartition de l'espace vertical
fenetre.grid_rowconfigure(1, weight=1)
fenetre.grid_columnconfigure(1, weight=1)

# Lie la fonction mettre_a_jour_liste à l'événement de changement de texte dans la recherche
recherche_entree.bind("<KeyRelease>", mettre_a_jour_liste)

# Lie la fonction afficher_details à la sélection dans la liste
algo_liste.bind("<<ListboxSelect>>", afficher_details)

fenetre.mainloop()
