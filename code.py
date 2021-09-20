import pandas as pd

responses = pd.read_csv('responses.csv')
# print(responses)

isAllocated = {}
topicOf = {}

for index,tuple in responses.iterrows():
    rollno = tuple['rollno']
    response = tuple['response']
    order = list(response.split(','))

    # remove leading and trailing spaces
    order = list(map(lambda x: x.strip(), order))

    # remove any non-numbers
    order = list(filter(lambda x: x.isdigit(), order))

    # convert to integers
    order = list(map(lambda x: int(x), order))

    # remove any integers not in range
    order = list(filter(lambda x: x>=1 and x<=144, order))

    # add remaining numbers
    remaining = list(filter(lambda x: x not in order, range(1,145)))
    order = order+remaining

    print(order)
    for topicno in order:
        if topicno not in isAllocated:
            topicOf[rollno] = topicno
            isAllocated[topicno] = True
            break

print(topicOf)
