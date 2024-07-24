import copy
ori_list=[[1,2,3],[4,5,6],[7,8,9]]
latter_list=copy.copy(ori_list)
latter_list[0]=[9,8,7]
print("old_list:",ori_list)
print("new_list:",latter_list)