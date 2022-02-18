

def max_activities(activities: list) -> list:
    """
    Input:
        activities: list of time of activities in format [start_time (int), end_time (int)]
    Output:
        list with max count of activities without intersections
    """
    activities.sort(key=lambda x: x[1])
    max_size_activities = [activities[0]]
    for i in range(1, len(activities)):
        if max_size_activities[-1][1] <= activities[i][0]:
            max_size_activities.append(activities[i])
    return max_size_activities
