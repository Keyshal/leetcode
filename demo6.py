# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def buildlist(self,head):
        tmphead = ListNode(head[0])
        # reshead = ListNode(head[0])
        reshead = tmphead
        lenh = len(head)
        for i in range(1, lenh):
            tmp = ListNode(head[i])
            tmphead.next = tmp
            tmphead = tmphead.next
        return reshead

    def deleteDup(self,head):
        tmp1=[]
        tmp2=[]
        tmphead=head
        try:
            while tmphead is not None:
                tmp1.append(tmphead.val)
                tmphead=tmphead.next
            ff = dict(collections.Counter(tmp1))
            for i in ff.items():
                if i[1] == 1:
                    tmp2.append(i[0])
            if len(tmp2)>0:
                reshead=self.buildlist(tmp2)
                return reshead
            else:
                return 
        except BaseException as e:
            print("haha")


   



    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # head = [1, 2, 3, 3, 4, 4, 5]
        # reshead=buildlist(head)
        reslist=self.deleteDup(head)
        return reslist
