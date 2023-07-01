import time
from win10toast import ToastNotifier
toaster = ToastNotifier()

# while True:
toaster.show_toast("গোসল টাইম!!",
                    "তোমার গোসল করার সময় হয়েছে !",
                    icon_path = None,
                    duration=2,
                    )

toaster.show_toast("দেরী কোরনা",
                    "এখনি গোসল করতে যাও ",
                    icon_path=None,
                    duration=2,
                    threaded=True
                    )
# Wait for threaded notification to finish
while toaster.notification_active(): time.sleep(18) 

toaster.show_toast("ধন্যবাদ!",
                    "তুমি ৩০ মিনিটের মধ্যে ফিরে এসেছো !",
                    icon_path = None,
                    duration=10)