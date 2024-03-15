def BezierSubdivision (ControlPoints, iterations, max_iterations):
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

def MidPoint(Point1, Point2):
    return ((Point1[0]+Point2[0]) * 0.5, (Point1[1]+Point2[1]) * 0.5)

def CheckDistance(Point1, Point2):
    return ((abs(Point1[0]-Point2[0])**2 + abs(Point1[1]-Point2[1])**2)**0.5)