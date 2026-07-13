class Solution:
	# @param A : head node of linked list
	# @return the head node in the linked list
	def solve(self, A):
		s = A 
		f = A 
		while True:
			s = s.next 
			f = f.next.next
            if s == f:
                break
		new = A 
		while new!=s:
			new = new.next 
			s = s.next 
		temp = s 
		while temp.next != s:
			temp = temp.next 
		temp.next = None 
		return A
        