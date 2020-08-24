# Sum Two Linked Lists

def sum_two_lists(self, llist):
    p = self.head  
    q = llist.head
    s = ""
    s1 = ""
    sum_llist = LinkedList()

    while p:
        s += str(p.data)
        p = p.next
        
    while q:
        s1 += str(q.data)
        q = q.next
        
    if s and s1:
        ans = str(int(s[::-1]) + int(s1[::-1]))
        for i in ans[::-1]:
            sum_llist.append(int(i))
    elif s:
        for i in s:
            sum_llist.append(int(i))
    else:
        for i in s1:
            sum_llist.append(int(i))
    return sum_llist