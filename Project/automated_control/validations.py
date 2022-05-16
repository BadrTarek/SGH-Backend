import datetime
from iot.models import ActuatorsAction



def check_date(product,actuator):
    
    try:
        difference  = datetime.datetime.now() - datetime.datetime.strptime( 
                    str(ActuatorsAction.get_last_automated_actions(product,actuator).created_at)[:19] , '%Y-%m-%d %H:%M:%S'
        )
    except:
        return True

    time = datetime.datetime.strptime ( str(product.time_between_automated_action) , '%H:%M:%S' )

    print("&" * 8)

    
    if  difference.total_seconds() < (time - datetime.datetime(1900, 1, 1)).total_seconds() :
        return False
    return True      
