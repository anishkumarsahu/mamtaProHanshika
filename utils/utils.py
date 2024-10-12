

import threading

import requests

from mamtaApp.models import WhatsappMessage, WhatsappMessageStatus


class MessageThread(threading.Thread):
    def __init__(self, number, message, partyName, collectionID,paymentType):
        self.number = number
        self.message = message
        self.partyName = partyName
        self.collectionID = collectionID
        self.paymentType = paymentType
        self._is_running = True
        threading.Thread.__init__(self)
    
        

    def run(self):
        while (self._is_running):
            msg = WhatsappMessage.objects.filter(isDeleted__exact=False).last()
            if msg.used < msg.balance:
                try:
                    url = msg.rootUrl + "send?number=91" + self.number + "&type=text&message=" + self.message + "&instance_id=" + msg.instanceID + "&access_token=" + msg.apiKey
                    r = requests.get( url,verify=False)
                    data = r.json()
                    obj = WhatsappMessageStatus()
                    obj.phone = self.number
                    obj.message = self.message
                    obj.messageTo = self.partyName
                    obj.collectionID = self.collectionID
                    obj.paymentType = self.paymentType
                    try:
                        if data['status'] == 'success' and data['message']:
                            obj.status = True
                        else:
                            obj.status = False
                    except:
                        obj.status = False
                    obj.save()

                    msg.used = (msg.used + 1)
                    msg.save()
                except:
                    obj = WhatsappMessageStatus()
                    obj.phone = self.number
                    obj.message = self.message
                    obj.messageTo = self.partyName
                    obj.collectionID = self.collectionID
                    obj.paymentType = self.paymentType
                    obj.status = False
                    obj.save()

            else:
                obj = WhatsappMessageStatus()
                obj.phone = self.number
                obj.message = self.message
                obj.messageTo = self.partyName
                obj.collectionID = self.collectionID
                obj.paymentType = self.paymentType
                obj.status = False
                obj.save()

            self.stop()

    def stop(self):
        self._is_running = False


def send_message(number, message, party, collectionID, paymentType="Cash"):
    MessageThread(number, message, party, collectionID, paymentType).start()