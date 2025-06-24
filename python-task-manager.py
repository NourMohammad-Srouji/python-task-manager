# defining queue functions
def insert(prio_queue, task):
    prio_queue.append(task)
    
    
def extract(prio_queue):
    if is_empty(prio_queue):
        return None

    highest_prio = prio_queue[0][2]
    highest_prio_index = 0
    for indx, ele in enumerate(prio_queue):
        if ele[2] < highest_prio:
            highest_prio = ele[2]
            highest_prio_index = indx
            
    return highest_prio_index

def peek(prio_queue, extract_highest_priority):
    if is_empty(prio_queue):
        return None
    return prio_queue[0] 
        
def is_empty(prio_queue):
    return len(prio_queue) == 0
