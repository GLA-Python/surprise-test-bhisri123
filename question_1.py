from numpy import format_float_positional


def expanding(l):
         diff= l[1]-l[0]
         for i in range(2,len(1)):
            if abs(l[i]-l[i-1])>diff:
                 diff=abs(l[i]-l[i-1])
                 return False
            else:
                 return True
