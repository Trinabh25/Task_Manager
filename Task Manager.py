from pywebio.input import *
from pywebio.output import *
from functools import partial


def completed(task, allTasks):
    allTasks.remove(task)
    clear("scope1")
    if len(allTasks) > 0:
        with use_scope("scope1"):
            put_table([[
                i["item"]["name"], i["item"]["content"],i["importance"], put_button('Complete', onclick=partial(
                    completed, task=i, allTasks=allTasks))
            ] for i in allTasks

            ],header=["Name", "Content", "Priority","Complete"]
            )


def task():
    with use_scope("scope1"):
        tasks = []
        while True:
            item = input_group(label="To do list", inputs=[
                input(label="Name", type="text", name="name"),
                input(label="Content", type="text", name="content"),
            ])
            importance = select(label="Select the tasks's priority", multiple=False, options=["High","Medium","Low"])
            tasks.append({"item" : item, "importance" : importance})
            clear("scope1")
            put_table([[
                i["item"]["name"], i["item"]["content"],i["importance"], put_button('Complete', onclick=partial(
                    completed, task=i, allTasks=tasks))
            ] for i in tasks

            ],header=["Name", "Content", "Priority","Complete"]
            )

task()


# completed(a,b)

# partial(completed,a,b)

# partial(completed,a=10,b=20)


# def abc(a,b,c):
#     pass

# partial(abc, a = 1,b=2,c=3)
