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

def complete_next_task(prio_queue):
         highest_priority_task =  extract(prio_queue)
         print('The next task with highest priority is:',  prio_queue[highest_priority_task][0])
         print("It's duration is",  prio_queue[highest_priority_task][1], 'minutes')
         print("It's priority is",  prio_queue[highest_priority_task][2])
         return highest_priority_task 

def insert_sort(prio_queue):
    for i in range(1, len(prio_queue)):
        key = prio_queue[i][0]
        temp = prio_queue[i]
        j = i - 1
        while j >= 0 and prio_queue[j][0] > key:
            prio_queue[j+1] = prio_queue[j]
            j -= 1
            prio_queue[j+1] = temp
  
    return prio_queue
    
def search_for_task(prio_queue, title):
    low = 0
    high = len(prio_queue) - 1

    Found = True
    while low <= high:
        mid = (low + high) // 2
    
        if prio_queue[mid][0].lower() == title:
            return Found, title
        elif prio_queue[mid][0].lower() < title:
            low = mid + 1
        else:
            high = mid - 1
    return not Found, title

def sort_tasks(L):
    if len(L) <= 1:
        return L

    mid = len(L) // 2
    left = sort_tasks(L[:mid])
    right = sort_tasks(L[mid:])

    return merge_sort(left, right)

def merge_sort(left, right):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i][1] < right[j][1]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
        
    return result

def main(num_of_tasks):
    while num_of_tasks <= 0:
        if num_of_tasks == 0:
            print('There is no tasks to be done.')
            break
        else:
            print('You entered invalid number of tasks.')
            num_of_tasks = int(input('Please enter a new valid number of tasks: '))

    for num in range(num_of_tasks):
        print('Task', num+1, ':')
        title = input('Enter the title for task ' + str(num+1) + ':')
        duration = int(input('Enter the task duration (in mins):'))
        while duration <= 0:
            print('This is an invalid duration of time')
            duration = int(input('Please enter a positive time in minutes: '))
        priority = int(input('Enter the priority for the task (lower value of priority the higher it is): '))
        task = (title, duration, priority)
        insert(prio_queue, task)

num_of_tasks = int(input('Enter the number of tasks you want to perform: '))

prio_queue = []