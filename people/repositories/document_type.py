from people.models import DocumentType


class DocumentTypeRepository:
    @staticmethod
    def get_all_document_types():
        return DocumentType.objects.all()
    
    @staticmethod
    def get_document_type_by_name(name):
        return DocumentType.objects.filter(name__icontains=name)