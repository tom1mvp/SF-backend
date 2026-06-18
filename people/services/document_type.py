from rest_framework.validators import ValidationError


from people.repositories.document_type import DocumentTypeRepository


class DocumentTypeServices:
    @staticmethod
    def get_all_document_types():
        return DocumentTypeRepository.get_all_document_types()
    
    @staticmethod
    def get_document_type_by_name(name):
        return DocumentTypeRepository.get_document_type_by_name(name)
    
    