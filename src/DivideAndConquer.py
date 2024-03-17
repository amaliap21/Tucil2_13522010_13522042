# def bezier_divide_and_conquer(points, reps, max_reps):
#     if reps == max_reps:
#         return points
#     else:
#         new_points = []
#         new_points.append(points[0])
#         for i in range(len(points) - 1):
#             x = 0.5 * points[i][0] + 0.5 * points[i + 1][0]
#             y = 0.5 * points[i][1] + 0.5 * points[i + 1][1]
#             new_points.append((x, y))
#         new_points.append(points[-1])
#         reps += 1
#         return bezier_divide_and_conquer(new_points, reps, max_reps)

def bezier_divide_and_conquer (ControlPoints, iterations, max_iterations):
    if iterations < max_iterations:
        #STEP 1: Calculate midpoints of each pair of control points
        Mids = []
        for i in range (len(ControlPoints)-1):
            Mids.append(MidPoint(ControlPoints[i], ControlPoints[i+1]))
        #STEP 2: Calculate points of the new curve
        Results = []
        Results.append(ControlPoints[0])
        for i in range (len(Mids)):
            Results.append(MidPoint(ControlPoints[i], Mids[i]))
            Results.append(MidPoint(Mids[i], ControlPoints[i+1]))
        Results.append(ControlPoints[-1])
        iterations += 1
        return Results, Mids

    # else: do nothing

#def bezier_divide_and_conquer2 (ControlPoints, Tolerance):
    #pass
    

def bezier_divide_and_conquer2 (ControlPoints, Tolerance):
        #STEP 1: Calculate first final point
        Results = []
        NewControl, Mids = ToThree(ControlPoints)
        #print("Mids:", Mids)
        #print("NewControl:", NewControl)

        #STEP 2: Check distance between result points
        LeftDist = CheckDistance(ControlPoints[0], NewControl)
        #print("LeftDist:", LeftDist)
        RightDist = CheckDistance(NewControl, ControlPoints[-1])
        #print("RightDist:", RightDist)

        #STEP 3: Recursively divide curve until it's under tolerance
        MidsLeft = []
        MidsRight = []
        if (LeftDist <= Tolerance):
            Results.append(ControlPoints[0])
            #print("CP0 Point:", ControlPoints[0])
            #print("CP0 appended:", Results)
            Results.append(NewControl)
            #print("NC:", Results)
        elif (LeftDist > Tolerance):
            Left = DivideCurveLeft(ControlPoints, NewControl, Mids)
            #print("Call recur left with", Left)
            NewControlsLeft, MidsLeft, MidsLeft2, MidsRight2 = bezier_divide_and_conquer2(Left, Tolerance)
            Results.extend(NewControlsLeft)

        if (RightDist <= Tolerance):
            #NewControl already added to Result, dont need to add it again
            Results.append(ControlPoints[-1])
            #print("CP-1:", Results)
        elif (RightDist > Tolerance):
            Right = DivideCurveRight(ControlPoints, NewControl, Mids)
            #print("Call recur right with", Right)
            NewControlRight, MidsRight, MidsLeft2, MidsRight2 = bezier_divide_and_conquer2(Right, Tolerance)
            Results.extend(NewControlRight)
        #print("Close enough!", ControlPoints, Results)
        return Results, Mids, MidsLeft, MidsRight

def ToThree (ControlPoints):
    if len(ControlPoints) == 3:
        Mids = [MidPoint(ControlPoints[0], ControlPoints[1]), MidPoint(ControlPoints[1], ControlPoints[2])]
        NewControl =  MidPoint(Mids[0], Mids[1])
        return NewControl, [Mids]
    else:
        #print("ControlPoints:", ControlPoints)
        Mids = []
        TempMid1 = []
        for i in range (len(ControlPoints)-1):
            TempMid1.append(MidPoint(ControlPoints[i], ControlPoints[i+1]))
        Mids.extend([TempMid1])
        #print(len(TempMid1), "TempMid1:", TempMid1)
        NewControl, TempMid = ToThree(TempMid1)
        Mids.extend(TempMid)
        return NewControl, Mids

def DivideCurveLeft (ControlPoints, NewControl, MiddlePoints):
    Left = [ControlPoints[0]]
    for i in range (len(MiddlePoints)):
        Left.append(MiddlePoints[i][0])
    Left.append(NewControl)
    return Left

def DivideCurveRight (ControlPoints, NewControl, MiddlePoints):
    Right = [NewControl]
    for i in range (len(MiddlePoints)):
        Right.append(MiddlePoints[i][-1])
    Right.append(ControlPoints[-1])
    return Right
   
def MidPoint(Point1, Point2):
    return ((Point1[0]+Point2[0]) * 0.5, (Point1[1]+Point2[1]) * 0.5)

def CheckDistance(Point1, Point2):
    return ((abs(Point1[0]-Point2[0])**2 + abs(Point1[1]-Point2[1])**2)**0.5)