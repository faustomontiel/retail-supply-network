from src.services.messageService import messageService, message
from src.services.companyService import CompanyService
from src.services.subscriptionService import SubscriptionService
from src.models.publication import Publication
from src.utils.logs import Logs, Error
from sqlalchemy.orm import Session


class PublicationService(messageService):
    def __init__(self, db: Session):
        super().__init__()
        self._db = db
        self._logs = Logs()
        self._error = Error()

    def createPublication(self, publicator: str, gtin: str, supplier: str, subscriber: str):
        try:
            companyService = CompanyService(self._db)
            subscriptionService = SubscriptionService(self._db)

            self._logs.doLog('Start publication create')

            if not companyService.is_supplier(publicator):
                return self._error._errorReturn(f'Company publicator {publicator} must be a supplier company in the system (PUB)', errorValidaror=True)

            if not companyService.company_exist(supplier):
                return self._error._errorReturn(f'Company supllier {supplier} not exist in RSN', errorValidaror=True)

            if not companyService.company_exist(subscriber):
                return self._error._errorReturn(f'Company subscriber {subscriber} not exist in RSN', errorValidaror=True)

            if not subscriptionService.subscription_exist(supplier, subscriber):
                return self._error._errorReturn(f'Subscription {supplier} -> {subscriber} not exist in RSN', errorValidaror=True)

            self._logs.doLog('Validation company OK.')

            publication = self._db.query(Publication).filter_by(gtin=gtin, supplier=supplier, subscriber=subscriber).first()

            if publication:
                publication.gtin = gtin
                publication.supplier = supplier
                publication.subscriber = subscriber
            else:
                publication = Publication(gtin=gtin, supplier=supplier, subscriber=subscriber)
                self._db.add(publication)

            self._db.commit()
            self._db.refresh(publication)


            return {'Success': True, 'publication_id': publication.id}
        except Exception as e:      
            self._db.rollback()
            self._logs.doLog("ERROR in createPublication(): " + str(e))
            return {'Error': str(e)}

class publicationMessage(message):
    def __init__(self):
        super().__init__()
