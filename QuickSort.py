class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def print_linked_list(head):
    current = head
    elements = []
    while current:
        elements.append(str(current.value))
        current = current.next
    print(" -> ".join(elements))

# Función de quicksort con opción para ordenar de forma ascendente o descendente
def quicksort_linked_list(head, ascending=True):
    if not head or not head.next:
        return head

    pivot = head  # Seleccionamos el primer nodo como pivote
    left_dummy = Node(None)  # Lista temporal para menores
    right_dummy = Node(None)  # Lista temporal para mayores
    left = left_dummy
    right = right_dummy
    current = head.next

    while current:
        if (ascending and current.value < pivot.value) or (not ascending and current.value > pivot.value):
            left.next = current
            left = left.next
        else:
            right.next = current
            right = right.next
        current = current.next

    left.next = None
    right.next = None

    # Ordenar recursivamente las sublistas
    sorted_left = quicksort_linked_list(left_dummy.next, ascending)
    sorted_right = quicksort_linked_list(right_dummy.next, ascending)

    # Unir las listas
    if sorted_left:
        tail = sorted_left
        while tail.next:
            tail = tail.next
        tail.next = pivot
    else:
        sorted_left = pivot

    pivot.next = sorted_right
    return sorted_left

# Función para convertir una lista de Python a lista enlazada
def list_to_linked_list(elements):
    if not elements:
        return None
    head = Node(elements[0])
    current = head
    for element in elements[1:]:
        current.next = Node(element)
        current = current.next
    return head

# Función para leer datos de un archivo y devolver lista de enteros o strings
def read_data_from_file(filename):
    with open(filename, 'r') as file:
        data = file.read()
        elements = data.replace(',', ' ').split()
        try:
            return [int(e) for e in elements]
        except ValueError:
            return elements

# Ejemplo de uso
if __name__ == "__main__":
    # Leer datos desde el archivo datos.txt
    filename = 'datos.txt'
    elements = read_data_from_file(filename)

    print("Datos originales desde el archivo:")
    print(elements)

    print("\nMétodo QuickSort:")
    # Convertir la lista en una lista enlazada
    linked_list_head = list_to_linked_list(elements)

    print("Lista enlazada original:")
    print_linked_list(linked_list_head)

    # Ordenar la lista enlazada en orden ascendente
    sorted_linked_list = quicksort_linked_list(linked_list_head, ascending=True)

    print("\nLista enlazada ordenada ascendentemente:")
    print_linked_list(sorted_linked_list)

    # Ordenar en orden descendente
    linked_list_head = list_to_linked_list(elements)
    sorted_linked_list_desc = quicksort_linked_list(linked_list_head, ascending=False)

    print("\nLista enlazada ordenada descendentemente:")
    print_linked_list(sorted_linked_list_desc)
