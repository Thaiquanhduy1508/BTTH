def Sequential_Search(dlist, item):
    """Tìm kiếm tuyến tính trong danh sách dlist."""
    for index, value in enumerate(dlist):
        if value == item:
            return (True, index)
    return (False, -1)
