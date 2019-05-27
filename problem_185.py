'''
Given two rectangles on a 2D graph, return the area of their intersection.
If the rectangles don't intersect, return 0.
'''

def area_of_intersect(r1,r2):
    r1_tl = r1['top_left']
    r1_br = (r1_tl[0]+r1['dimensions'][0],r1_tl[1]+r1['dimensions'][1])

    r2_tl = r2['top_left']
    r2_br = (r2_tl[0]+r2['dimensions'][0],r2_tl[1]+r2['dimensions'][1])

    if r1_br[0] <= r2_tl[0] or r2_br[0] <=r1_tl[0]:
        return 0

    if r1_br[1] <= r2_tl[1] or r2_br[1] <= r1_tl[1]:
        return 0

    in_tl = (max(r1_tl[0],r2_tl[0]),max(r1_tl[1],r2_tl[1]))

    in_br = (min(r1_br[0],r2_br[0]),min(r1_br[1],r2_br[1]))

    in_d = (abs(in_br[0] - in_tl[0]), abs(in_br[1]- in_tl[1]))

    return in_d[0]*in_d[1]

print(area_of_intersect({'top_left':[1,4],'dimensions':[3,3]},{'top_left':[0,5],'dimensions':[4,3]}))
