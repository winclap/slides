
def schedule_function(event, context):
    print("Hola PyConAr a las {}".format(event.get('time')))
