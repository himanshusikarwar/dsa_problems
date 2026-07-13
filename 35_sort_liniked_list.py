class Solution:
	# @param A : head node of linked list
	# @return the head node in the linked list
	def sortList(self, A):
		def merge(h1, h2):
			fh = ListNode(-1) 
			temp = fh
			while h1 and h2:
				if h1.val < h2.val:
					temp.next = ListNode(h1.val)
					h1 = h1.next 
				else:
					temp.next = ListNode(h2.val)
					h2 = h2.next 
				temp = temp.next 
			if h1:
				temp.next = h1 
			if h2:
				temp.next= h2 
			return fh.next 
		def merge_sort(A):
			if A is None or A.next is None:
				return A
			s = A 
			f = A
			while f.next and f.next.next:
				s = s.next 
				f = f.next.next 
			mid = s 
			h2 = mid.next 
			mid.next = None 
			h1 = merge_sort(A)
			h2 = merge_sort(h2)
			fh = merge(h1, h2)
			return fh 
        return merge_sort(A)
		
        