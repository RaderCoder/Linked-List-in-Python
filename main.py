# For Testing
import LinkedList

if __name__ == "__main__":
    New_list = LinkedList.LinkedList(6)
    New_list.push(5)
    New_list.push(3)

    print(New_list)

    print(New_list.find_value(5))

    print(New_list.find_value(4))

    New_list.delete_node(4)

    New_list.delete_node(3)

    print(New_list)