def bezier_divide_and_conquer(ControlPoints, Tolerance):
        #STEP 1: Calculate first final point
        Results = []
        NewControl, Mids = ToThree(ControlPoints)

        #STEP 2: Check distance between result points
        LeftDist = CheckDistance(ControlPoints[0], NewControl)
        RightDist = CheckDistance(NewControl, ControlPoints[-1])

        #STEP 3: Recursively divide curve until it's under tolerance
        MidsLeft = []
        MidsRight = []
        if (LeftDist <= Tolerance):
            Results.append(ControlPoints[0])
            Results.append(NewControl)
        elif (LeftDist > Tolerance):
            Left = DivideCurveLeft(ControlPoints, NewControl, Mids)
            NewControlsLeft, MidsLeft, MidsLeft2, MidsRight2 = bezier_divide_and_conquer(Left, Tolerance)
            Results.extend(NewControlsLeft)

        if (RightDist <= Tolerance):
            #NewControl already added to Result, dont need to add it again
            Results.append(ControlPoints[-1])
            pass
        elif (RightDist > Tolerance):
            Right = DivideCurveRight(ControlPoints, NewControl, Mids)
            NewControlRight, MidsRight, MidsLeft2, MidsRight2 = bezier_divide_and_conquer(Right, Tolerance)
            Results.extend(NewControlRight)
        return Results, Mids, MidsLeft, MidsRight

def ToThree (ControlPoints):
    if len(ControlPoints) == 3:
        Mids = [MidPoint(ControlPoints[0], ControlPoints[1]), MidPoint(ControlPoints[1], ControlPoints[2])]
        NewControl =  MidPoint(Mids[0], Mids[1])
        return NewControl, [Mids]
    else:
        Mids = []
        TempMid1 = []
        for i in range (len(ControlPoints)-1):
            TempMid1.append(MidPoint(ControlPoints[i], ControlPoints[i+1]))
        Mids.extend([TempMid1])
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
    for i in reversed(MiddlePoints):
        Right.append(i[-1])
    Right.append(ControlPoints[-1])
    return Right

def MidPoint(Point1, Point2):
    return ((Point1[0]+Point2[0]) * 0.5, (Point1[1]+Point2[1]) * 0.5)

def CheckDistance(Point1, Point2):
    return ((abs(Point1[0]-Point2[0])**2 + abs(Point1[1]-Point2[1])**2)**0.5)