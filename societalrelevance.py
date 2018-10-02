import random

Relevant_Jobs = ['Doctor', 'Engineer', 'Lawyer', 'Banker', 'Entreprenuer', 'Professor', 'Politician', ]
Irrelevant_jobs = ['Musician', 'Athlete', 'Philosopher', 'Writer', 'Carpentry', 'Bricklaying', 'Artist', 'Cook', 'Gardener']

Citizens = []
No_of_working_age = 3

irrelevant_no = range(0, 12)
relevant_no = range(13, 25)
#y = 0
#x = 0


while len(Citizens) < 5:
    Candidates = input('input your name ')
    Citizens.append(Candidates)
    print(Citizens)

    appointed_candidate = random.choice(Citizens)
    print(appointed_candidate)

    name_index = len(Candidates)
    low_job = random.choice(Irrelevant_jobs)
    high_job = random.choice(Relevant_Jobs)

    # if name_index <= irrelevant_no:
    #     print('You will now be: ', low_job)
    # else:
    #     print('You will now be: ', high_job)

    for x in irrelevant_no:
        if name_index is x:
            print('you wil now be:', low_job)
        else:
            pass
    for a in relevant_no:
        if name_index is a:
            print('You will now be: ', high_job)
        else:
            pass


    '''for y in relevant_no:
        if name_index is y:
            print('{0} you are now a {1}'.format(Citizens, high_job))
        else:
            print('The must be an error, please follow the officer approaching you to hte nearest Odessey station')
'''