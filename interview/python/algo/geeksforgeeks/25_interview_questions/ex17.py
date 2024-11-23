# Find if two rectangles overlap
#
# Given two rectangles, find if the given two rectangles overlap or not.
# Note that a rectangle can be represented by two coordinates, top left and bottom right.
# So mainly we are given following four coordinates.
# l1: Top Left coordinate of first rectangle.
# r1: Bottom Right coordinate of first rectangle.
# l2: Top Left coordinate of second rectangle.
# r2: Bottom Right coordinate of second rectangle.
#
#
# We need to write a function bool doOverlap(l1, r1, l2, r2) that
# returns true if the two given rectangles overlap.
#
# https://www.geeksforgeeks.org/find-two-rectangles-overlap/
# https://www.youtube.com/watch?v=zGv3hOORxh0

# Input: rec1 = ((r1x1,r1y1), (r1x2,r1,y2)), rec2 = ((r2x1,r2y1), (r2x2,r2,y2))
def is_overlap(rec1, rec2):
    r1lx, r1ly = rec1[0]
    r1rx, r1ry = rec1[1]

    r2lx, r2ly = rec2[0]
    r2rx, r2ry = rec2[1]

    if r1lx > r2rx or r2lx > r1rx:
        return False

    if r1ly < r2ry or r2ly < r1ry:
        return False

    return True

rec1 = ((0,10), (10,0))
rec2 = ((5,5), (15,0))

print (is_overlap(rec1, rec2))
