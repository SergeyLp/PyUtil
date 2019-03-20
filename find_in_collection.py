def find_one(x, Q, start: int, end: int) -> int:
    ''' x  What finding, must have len() 
       Q  Collection for finding
       start index of first where been startin search
       end index until searching is doing
       return index first found element in collection Q
    '''
    try:
        return Q.index(x, start, end)
    except ValueError:
        return None

def find_whole(x, Q) -> bool:
     ''' x  What finding, must have len() 
        Q  Collection for finding
     '''
     iq = 0     #счетчик по элементам множества
     x_end = len(x)
     iq_end = len(Q) - x_end + 1   #индекс элемента до которого имеет смысл искать
     while iq < iq_end:
         iq = find_one(x[0], Q, iq, iq_end)    # индекс первого искомого
         if iq is None:
             return False

         for ix in range(1, x_end) :    # Счетчик по элеметам искомого
            found_i = find_one(x[ix], Q, iq+1, iq_end+ix)
            if found_i is not None and found_i == iq + 1:
                iq = found_i
            else:
                iq += 1
                break # Счетчик по элеметам искомого, но остаёмся внутри счётчика по элементам множества

         else:  #good ended (found all elements)
             return True

     return False 
     
     
def is_all_in(Qx, Q)->bool:
'''Return true if all elements of Qx
   exist in Q
'''
  for x in Q:
   if x not in Qx:
       return False

  return True
     

if __name__ == '__main__':
    s = [("1012","1013","1012","1013","1014", ),('1000',), ('1001','1002'),
         ('1003', '1004', '1005'), ('1006', '1007', '1008', '1009'),
         ("1010","1011","1012","1013","1014"), ('1000','1000','1000,1000'),
         ('1012','1013','1012','1013','1014', '1015'), ('2002','2002'), ('2003','2003','2003'),
         ('2004', '2004','2004', '2004'), ('3001', '3000', '3001'), ('4001','4000', '4000', '4001'),
         ('4002', '4002', '4003', '4003'), ('4004','4004','4004','4005'), tuple()]

    t = [("1000",), ('1001',), ('1001', '1002'), ('1000','1000'),("1012","1013", "1014"),
         ('2002','2002'), ('2003','2003')]

    for ti in t:
        for y in s:
            if find_whole(ti, y):
                print(ti , 'in', y)

