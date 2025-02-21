# 40. Afghanistan has surrounded by attackers. A truck enters the city. The driver claims the load is food and medicine from
# Pakistanis. Yasir is one of the soldier in Afghanistan. He doubts about the truck, maybe it •s from the siege. He knows that a tag is
# valid if the sum of every two consecutive digits of it is even and its letter is not a vowel. If the tag is invalid then Yasir need
# to arrest the driver of the truck with invalid tab. If it is valid the truck is allowed inside the country. Can you help in
# determine if he need to arrest or allow the truck?

def is_valid_tag(tag):
  vowels = 'AEIOU'
  
  for i in range(len(tag)-1):
    if tag[i].isdigit() and tag[i+1].isdigit():
      if (int(tag[i]) + int(tag[i + 1])) %2 !=0:
        return False
        
        
  
  for char in tag:
    if char.isalpha() and char.upper() in vowels:
      return False
      
  return True
  
tag = "1135b"
if is_valid_tag(tag):
    print("allow the truck")
    
else:
    print("arrest the driver")
    
    
    


# 22. Once N Men and M Women attended a matrimonial event. The event is represented by a matrix named "a" of N rows and M columns where
# AU is 1 if the Men likes the Women Otherwise it will be O. Note that it is not necessary that if a Men x likes Women y, then
# Women y should like Men x. If there are two different Men x and y, who both like Women z, then there will be a collision. Can you
# calculate the number of different collisions in the matrimonial event? Note that order of Men in the collision doesn't matter.


def count_collisions(a):
    N = len(a)
    M = len(a[0])
    collisions = 0

    for j in range(M):
        count = 0
        for i in range(N):
            if a[i][j] == 1:
                count += 1
        if count > 1:
            collisions += (count * (count - 1)) // 2

    return collisions

# Example usage:
a = [
    [1, 0, 1],
    [0, 1, 1],
    [1, 1, 0]
]
print(count_collisions(a))  # Output: 3


# 33 Every day, Selvan goes to his office by train and
# buys the ticket from the counter on the day of travel. On the ticket, there is a
# letter-code that is represented as a string of upper-case Latin letters. Selvan believes that the day will be successful in case
# exactly two different letters in the code alternate.
# Otherwise, he believes that the day will be unlucky. Please see note section for
# formal definition of alternating code. If the ticket
# code is given. Please determine, whether the day will be successful for Selvan
# or not. Print "Successful Day" or "Unsuccessful Day"
# (without quotes) corresponding to the situation.


def is_successful_day(code):
    if len(code) < 2:
        return "Unsuccessful Day"

    first_char = code[0]
    second_char = None

    for i in range(1, len(code)):
        if code[i] != first_char:
            second_char = code[i]
            break

    if second_char is None:
        return "Unsuccessful Day"

    for i in range(len(code)):
        if i % 2 == 0:
            if code[i] != first_char:
                return "Unsuccessful Day"
        else:
            if code[i] != second_char:
                return "Unsuccessful Day"

    return "Successful Day"

# Example usage:
ticket_code = "ABABAB"
print(is_successful_day(ticket_code))  # Output: Successful Day

ticket_code = "AABBA"
print(is_successful_day(ticket_code))  # Output: Unsuccessful Day



# 37 Mohit has no work to do in the kitchen, so he decided to play a card game with the following rules: Initially, N cards are placed
# in a row on a table. Each card is placed either face up or face down. The goal of the game is to remove all cards from the table, one
# by one. A card may be removed only if it is currently facing up. When a card is removed, its adjacent cards (the cards directly to
# its left and right, if they exist) are flipped, i.e. a card that was facing up will be facing down and vice versa. There is an empty
# space left behind each removed card, i.e. the remaining cards are not moved to create a contiguous row of cards again. Therefore, if
# the game starts with three cards and the middle card is removed, then the cards on the sides are flipped, but removing one of these
# cards afterwards does not cause the other card to be flipped, since it is only adjacent to the empty space created by removing the
# middle card. Determine whether Mohit is able to win this game. 38 Jefecsgn was given a string s of length 8 consisting solely of 'O's
# and '1 is. Assume that the characters of the string are written in a circular fashion. Jeferson need to find the number of 0-1 or 1-0



def can_win_game(cards):
    def flip(card):
        return 'U' if card == 'D' else 'D'

    def remove_card(cards, index):
        if cards[index] == 'U':
            if index > 0:
                cards[index - 1] = flip(cards[index - 1])
            if index < len(cards) - 1:
                cards[index + 1] = flip(cards[index + 1])   
            cards[index] = 'E'  # E stands for empty
            return True
        return False

    while 'U' in cards:
        for i in range(len(cards)):
            if remove_card(cards, i):
                break
        else:
            return False
    return True

# Example usage:
cards = ['U', 'D', 'U']
print(can_win_game(cards))  # Output: True

cards = ['D', 'D', 'U']
print(can_win_game(cards))  # Output: False    
    
#2nd program

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class SingleLinkedList:
    def __init__(self):
        self.head = None
        
    def add_node(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        
    def prepend(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        
    def insert_after(self,prev_node,data):
        current = self.head
        while current and current.data != prev_node:
            current = current.next
        if not current:
            print("Node not found")
            return
        
        new_node = Node(data)
        new_node.next = current.next
        current.next = new_node
        
    def delete_node(self,key):
        current = self.head
        if current and current.data == key:
            self.head = current.next
            current = None
            return
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next
        if not current:
            print(f'Nosw with data {key} not found')
            return
        prev.next = current.next
        current = None
        
    def print_list(self):
        current = self.head
        while current:
            print(current.data,end='->')
            current = current.next
        print()
        
        
s1 = SingleLinkedList()
s1.add_node(1)
s1.add_node(2)
s1.add_node(3)
print("Original List")
s1.print_list()
s1.prepend(4)
print("After adding 4 at the end")  
s1.print_list()
s1.insert_after(2,5)
print("After adding 5 after 2")
s1.print_list()
s1.delete_node(2)
print("After deleting 2")
s1.print_list()      


#double linked list
class DNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, data):
        new_node = DNode(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        new_node.prev = last

    def prepend(self, data):
        new_node = DNode(data)
        if self.head is None:
            self.head = new_node
            return
        self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node

    def insert_after(self, prev_node_data, data):
        current = self.head
        while current and current.data != prev_node_data:
            current = current.next
        if not current:
            print("Node not found")
            return
        new_node = DNode(data)
        new_node.next = current.next
        new_node.prev = current
        if current.next:
            current.next.prev = new_node
        current.next = new_node

    def delete_node(self, key):
        current = self.head
        while current and current.data != key:
            current = current.next
        if not current:
            print(f'Node with data {key} not found')
            return
        if current.prev:
            current.prev.next = current.next
        if current.next:
            current.next.prev = current.prev
        if current == self.head:
            self.head = current.next
        current = None

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=' <-> ')
            current = current.next
        print()

# Example usage:
d1 = DoubleLinkedList()
d1.add_node(1)
d1.add_node(2)
d1.add_node(3)
print("Original List")
d1.print_list()
d1.prepend(4)
print("After adding 4 at the beginning")
d1.print_list()
d1.insert_after(2, 5)
print("After adding 5 after 2")
d1.print_list()
d1.delete_node(2)
print("After deleting 2")
d1.print_list()



#circulat linked list

class CNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, data):
        new_node = CNode(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return
        last = self.head
        while last.next != self.head:
            last = last.next
        last.next = new_node
        new_node.next = self.head

    def prepend(self, data):
        new_node = CNode(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return
        new_node.next = self.head
        last = self.head
        while last.next != self.head:
            last = last.next
        last.next = new_node
        self.head = new_node

    def insert_after(self, prev_node_data, data):
        current = self.head
        while current and current.data != prev_node_data:
            current = current.next
            if current == self.head:
                print("Node not found")
                return
        new_node = CNode(data)
        new_node.next = current.next
        current.next = new_node

    def delete_node(self, key):
        if self.head is None:
            print(f'Node with data {key} not found')
            return
        current = self.head
        prev = None
        while True:
            if current.data == key:
                if prev:
                    prev.next = current.next
                else:
                    if current.next == self.head:
                        self.head = None
                    else:
                        last = self.head
                        while last.next != self.head:
                            last = last.next
                        last.next = current.next
                        self.head = current.next
                current = None
                return
            prev = current
            current = current.next
            if current == self.head:
                break
        print(f'Node with data {key} not found')

    def print_list(self):
        if self.head is None:
            print("List is empty")
            return
        current = self.head
        while True:
            print(current.data, end=' -> ')
            current = current.next
            if current == self.head:
                break
        print()

# Example usage:
c1 = CircularLinkedList()
c1.add_node(1)
c1.add_node(2)
c1.add_node(3)
print("Original List")
c1.print_list()
c1.prepend(4)
print("After adding 4 at the beginning")
c1.print_list()
c1.insert_after(2, 5)
print("After adding 5 after 2")
c1.print_list()
c1.delete_node(2)
print("After deleting 2")
c1.print_list()             