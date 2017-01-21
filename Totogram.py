import sys

#main function of the Totogram
def main():
    ''' Divide the Midlist into two sub-list. A "left-sub-list" and a "Right-sub-list" . The number present at the middle
    is denoted as the "node". Thus it returns "Left-sub-list" ; "Right-sub-list" ;and "Node".'''
    
    def midlistfunction(l):
        leftlist=[]
        rightlist=[]
        node=[]
        node.append(l[(len(l)-1)/2])
        for i in range(0,((len(l)-1)/2)):
            leftlist.append(l[i])
        for i in range(((len(l)-1)/2)+1,len(l)):
            rightlist.append(l[i])
        return node,leftlist,rightlist
    
    
    ''' Sort a list into reverse order (5 4 3 2 1)'''
    
    def reverse_sort(x,y):
        return y-x
    
    ''' Sort a list into natural order order (1 2 3 4 5)'''
    def natural_sort(x,y):
        return x-y
    
    ''' Function to flatten a list [1 2 3 [4 5] 6]--->[1 2 3 4 5 6] '''
    
    def flatten(seq):
        res = []
        for item in seq:
            if (isinstance(item, (tuple, list))):
                res.extend(flatten(item))
            else:
                res.append(item)
        return res
    
    ''' Function to find all the elements at a particular depth in the tree structure '''
    
    def elements_at_depth_complete(ls,depth):
        treedepth=[]
        treedepth.append(ls[0])
        treedepth.append([ls[1],ls[2],ls[3]])
        depthmultiplier=3
        temp=0
        for i in range (2,k):
            temp=temp+depthmultiplier
            depthmultiplier=depthmultiplier*2
            templist=[]
            for j in range (1,depthmultiplier+1):
                templist.append(ls[temp+j])            
            treedepth.append(templist)
        return treedepth[depth]
    
    ''' Function to arrange a binary tree based on there depth. For example all the elements at depth 0, all the elements at
    depth1 and so on. It returns a list of list which contains all the elements of the binary tree structure at all the possible
    depths '''
    
    def elements_at_depth_binary_sublist(ls):
        treedepth=[]
        temp=0
        for i in range (0,k-1):
            templist=[]
            for j in range (0,2**i):
                templist.append(ls[temp+j])
            treedepth.append(templist)
            temp=temp+j+1
        return treedepth        
    
    ''' Function that returns the a map(known as dictionary in Python) of elements, which has "distance from parent", "Distance from first child" and 
    "Distance from second child" as the values '''
    
    def parent_child_distance(ls,node):
        parentchilddistance={}
        childparentmap={}
        counter=0
        i=0
        for i in range (0,len(ls)-1):
            childparentmap.update({ls[counter+1]:ls[i]})
            childparentmap.update({ls[counter+2]:ls[i]})
            if(ls[len(ls)-1]==ls[counter+2]):
                break
            if(i>0):
                node=childparentmap[ls[i]]
            parentchilddistance.update({ls[i] :((abs(node-ls[i])),(abs(ls[i]-ls[counter+1])),(abs(ls[i]-ls[counter+2])))})
            counter=counter+2
        parentchilddistance.update({ls[i] :((abs(node-ls[i])),(abs(ls[i]-ls[counter+1])),(abs(ls[i]-ls[counter+2])))})
        for i in range (i+1,len(ls)):
            node=childparentmap[ls[i]]
            parentchilddistance.update({ls[i] :((abs(node-ls[i])),0,0)})
        return parentchilddistance 
    
    
    ''' Elements from the Left-list are compared with the left child branch of the Mid-list elements and are swapped
    to minimize the distance between successive nodes'''
    
    
    def swap_leftlist_elements(leftlist,midlist,k):
        if (k>4):
            z= 2**(k-3)-(2**(k-5))
        else:
            z= 2**(k-3)
        
        
        temp=midlist[midlist.index(leftlist[0]+z)]  
        midlist[midlist.index(leftlist[0]+z)]=leftlist[0]
        leftlist[0]=temp 
        return leftlist,midlist
        
        ''' Elements from the Right-list are compared with the right child branch of the Mid-list elements and are swapped
            to minimize the distance between successive nodes'''
         
    def swap_rightlist_elements(rightlist,midlist,k):
        if (k>4):
            z= 2**(k-3)-(2**(k-5))
        else:
            z= 2**(k-3)
        
        temp=midlist[midlist.index(rightlist[0]-z)]
        midlist[midlist.index(rightlist[0]-z)]=rightlist[0]
        rightlist[0]=temp
        return rightlist,midlist
    
    ''' Create the left child list from the entire state space and optimize the distance between the successive nodes
     and returns back the left child list of the totogram tree structure'''
    
    def left_list_items(k,midlist):
        leftlist=[]
        element=(3*(2**(k-1)))-2
        midnumber=(element-1)/3 
        for i in range (1,midnumber+1):
            leftlist.append(i)    
            leftlist= sorted(leftlist, cmp=reverse_sort)
        
        leftlist,midlist=swap_leftlist_elements(leftlist,midlist,k)
        element_at_particulat_node=elements_at_depth_binary_sublist(leftlist)
         
        for a in range (len(element_at_particulat_node)-2,0,-1):
            temp1=[]
            temp2=[]
            temp1=sorted(element_at_particulat_node[a], cmp=reverse_sort)
            temp2=sorted(element_at_particulat_node[a+1], cmp=reverse_sort)
            for b in range (0,a):
                s=temp2[b] 
                temp2[b]=temp1[len(temp1)-1-b]
                temp1[len(temp1)-1-b]=s   
            element_at_particulat_node[a]=sorted(temp1, cmp=natural_sort)
            element_at_particulat_node[a+1]=sorted(temp2, cmp=natural_sort)
        leftlist=flatten(element_at_particulat_node)
        return leftlist
    
    ''' Create the mid child list from the entire state space and optimize the distance between the successive nodes
     and returns back the mid child list of the totogram tree structure'''
    
    def mid_list_items(k,rootnode):
        midlist=[]
        midleftlist=[]
        midrightlist=[]
        element=(3*(2**(k-1)))-2
        midnumber=(element-1)/3
        for i in range (midnumber+1,midnumber+midnumber+2):
            midlist.append(i)
        midlist.remove(rootnode)
    
        node,midleftlist,midrightlist=midlistfunction(midlist)
        midlist=node
        midleftlist=sorted(midleftlist, cmp=reverse_sort)
        midrightlist=sorted(midrightlist, cmp=natural_sort)
        pow2 = [2 ** x for x in range(k-2)]
        for j in range (0,len(pow2)):
            templeftlist=[]
            temprightlist=[]
            for i in range (0,pow2[j]):
                midlist.append(midleftlist[i])
                templeftlist.append(midleftlist[i])
            midleftlist = [y for y in midleftlist if y not in templeftlist]
             
            for i in range (0,pow2[j]):
                midlist.append(midrightlist[i])
                temprightlist.append(midrightlist[i])
            midrightlist = [y for y in midrightlist if y not in temprightlist]
        return midlist
    
    ''' Create the right child list from the entire state space and optimize the distance between the successive nodes
     and returns back the right child list of the totogram tree structure'''
    
    def right_list_items(k,midlist):
        rightlist=[]
        element=(3*(2**(k-1)))-2
        midnumber=(element-1)/3
        for r in range (midnumber+midnumber+2,element+1):
            rightlist.append(r) 
        rightlist= sorted(rightlist, cmp=natural_sort)
    
        rightlist,midlist=swap_rightlist_elements(rightlist,midlist,k)
        element_at_particulat_node=elements_at_depth_binary_sublist(rightlist)
        for a in range (len(element_at_particulat_node)-2,0,-1):
            temp1=[]
            temp2=[]
            temp1=element_at_particulat_node[a]
            temp2=element_at_particulat_node[a+1]
            for b in range (0,a):
                s=temp1[len(temp1)-1-b] 
                temp1[len(temp1)-1-b]=temp2[b]
                temp2[b]=s   
            element_at_particulat_node[a]=sorted(temp1, cmp=natural_sort)
            element_at_particulat_node[a+1]=sorted(temp2, cmp=natural_sort)
        rightlist=flatten(element_at_particulat_node)
        return rightlist
    
    ''' Create the complete Totogram tree structure based on the root-node, left-child-list, mid-child-list and 
    right-child-list. It returns back the Totogram in a list format '''
    
    def create_complete_list(rootnode,leftlist,midlist,rightlist):
        complete=[]
        complete.append(rootnode)
        pow2 = [2 ** x for x in range(k-1)]
        for j in range (0,len(pow2)):
            templeftlist=[]
            tempmidlist=[]
            temprightlist=[]
            for i in range (0,pow2[j]):
                templeftlist.append(leftlist[i])
            complete.append(sorted(templeftlist, cmp=natural_sort))
            leftlist = [y for y in leftlist if y not in templeftlist]  
            for i in range (0,pow2[j]):
                tempmidlist.append(midlist[i])
            complete.append(sorted(tempmidlist, cmp=natural_sort))
            midlist = [y for y in midlist if y not in tempmidlist]
            for i in range (0,pow2[j]):
                temprightlist.append(rightlist[i])
            complete.append(sorted(temprightlist, cmp=natural_sort))
            rightlist = [y for y in rightlist if y not in temprightlist] 
        complete=flatten(complete)
        return complete
    
    ''' Prints the elements in a list '''
    
    def print_complete_list(complete):
        for p in complete:
            print p,

    if len(sys.argv)!=2:
        print "Invalid Input"
        sys.exit()
    else:
        if sys.argv[1].isdigit():
            k=int(sys.argv[1])
        else:
            print "Enter number value for k"
            sys.exit()
    complete=[]
    leftlist=[]
    midlist=[]
    rightlist=[]
    parentchilddistance={}
    listofdistancebetwn_success_nodes=[]
    element_at_particulat_node=[]
    element=(3*(2**(k-1)))-2
    rootnode=element/2;    
     
    midlist=mid_list_items(k,rootnode)
    leftlist=left_list_items(k,midlist)
    rightlist=right_list_items(k,midlist)
    complete=create_complete_list(rootnode,leftlist,midlist,rightlist)
    
    ''' List of distances from parents to child '''
    parentchilddistance=parent_child_distance(leftlist,rootnode)     
    listofdistancebetwn_success_nodes.append(parentchilddistance.values())
    parentchilddistance=parent_child_distance(midlist,rootnode) 
    listofdistancebetwn_success_nodes.append(parentchilddistance.values())
    parentchilddistance=parent_child_distance(rightlist,rootnode) 
    listofdistancebetwn_success_nodes.append(parentchilddistance.values())
    
    ''' Finds the maximum value from the above mentioned list(parent-child-distance list) '''
    listofdistancebetwn_success_nodes=flatten(listofdistancebetwn_success_nodes)
    print max(listofdistancebetwn_success_nodes)
    print_complete_list(complete)  
    
main()       
    
    
    
        
                
    
    
