from datetime import datetime

def sample_messages(user_msg):
    user_msg = str(user_msg).lower()

    if user_msg in ('hello','hi'):
        return 'hey,hi'

    if user_msg in ('how are you'):
        return "I'm fine,how are you?"

    if user_msg in ("I'm fine"):
        return 'that\'s good'

    if user_msg in ('time'):
        now = datetime.now()
        date_time = now.strftime("%d/%m/%y", "%H:%M:%S") 

        return str(date_time)

    return "sorry I didn't get you"