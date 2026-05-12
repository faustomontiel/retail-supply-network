from src.services.messageService import messageService, message
from src.services.companyService import CompanyService
from src.models.subscription import Subscription
from src.utils.logs import Logs, Error
from sqlalchemy.orm import Session

class SubscriptionService(messageService):
    def __init__(self, db: Session):
        super().__init__()
        self._db = db
        self._logs = Logs()
        self._error = Error()

    def createSubscription(self, consultant: str, supplier: str, subscriber: str):
        try:
            self._logs.doLog(f"Start create Subscription")
            
            companyService = CompanyService(self._db)

            if len(supplier) < 10 or len(subscriber) < 10:
                return self._error._errorReturn('GLN must be at least 10 characters.',errorValidaror=True)

            if not companyService.company_exist(supplier):
                return self._error._errorReturn(f'Company {supplier} not registered in RSP.',exist=True)

            if not companyService.company_exist(subscriber):
                return self._error._errorReturn(f'Company {subscriber} not registered in RSP.',exist=True)

            if not companyService.is_subscriber(consultant):
                return self._error._errorReturn(f'Company {consultant} is not a Subscriber.',errorValidaror=True)

            if self.subscription_exist(supplier, subscriber):
                return self._error._errorReturn(f'Subscription {subscriber} -> {supplier} alredy exist.',errorValidaror=True)

            self._logs.doLog(f"Subscription validations OK.")

            subscription = Subscription(supplier=supplier, subscriber=subscriber)
            self._db.add(subscription)
            self._db.commit()
            self._db.refresh(subscription)

            self._logs.doLog(f"subscription added (Commit).")

            return {'success':True, 'subscription_id': subscription.id}
        except Exception as e:
            self._db.rollback()
            self._logs.doLog("ERROR createsubscription(): " + str(e))
            return {'error': str(e)}

    def subscription_exist(self, supplier: str, subscriber: str):
        subscription = self._db.query(Subscription).filter((Subscription.supplier == supplier) & (Subscription.subscriber == subscriber)).first()
        return subscription is not None

class subscriptionMessage(message):
    def __init__(self):
        super().__init__()
