from pdf4me.helper.pdf4me_exceptions import Pdf4meClientException
from pdf4me.helper.response_checker import ResponseChecker
from pdf4me.model import ConvertToPdf


class ConvertClient(object):

    def __init__(self, pdf4me_client):
        self.pdf4me_client = pdf4me_client

    def convert_to_pdf(self, convert_to_pdf):
        """The predefined convert_to_pdf is carried out.

        :param convert_to_pdf: PDF conversion configuration
        :type convert_to_pdf: ConvertToPdf
        :return: ConvertToPdfRes, contains generated PDF
        """

        # check convert_to_pdf validity
        self.__check_convert_to_pdf_object_validity(convert_to_pdf)

        res = self.pdf4me_client.custom_http.post_universal_object(universal_object=convert_to_pdf,
                                                                 controller='Convert/ConvertToPdf')

        # check response for errors
        ResponseChecker().check_document_for_errors(res)

        return res

    def convert_file_to_pdf(self, file, file_name):
        """The provided Non-PDF file gets converted to a PDF.

        :param file: to be converted to PDF
        :type file: file handler, use the method get_file_handler from FileReader to obtain it
        :param file_name: the name of the provided file (including the file extension)
        :type file_name: str
        :return: bytes of resulting PDF file, can be directly written to file on disk
        """

        streams = [('file', file)]
        params = [('fileName', file_name)]

        return self.pdf4me_client.custom_http.post_wrapper(octet_streams=streams, values=params,
                                                          controller='Convert/ConvertFileToPdf')

    def __check_convert_to_pdf_object_validity(self, convert_to_pdf):
        """Checks whether the convert_to_pdf object contains the essential information to be
                processed by the server."""

        if convert_to_pdf is None:
            raise Pdf4meClientException('The convert_to_pdf parameter cannot be None.')
        elif convert_to_pdf.document is None or convert_to_pdf.document.doc_data is None:
            raise Pdf4meClientException('The convert_to_pdf document cannot be None.')
        elif convert_to_pdf.convert_to_pdf_action is None:
            raise Pdf4meClientException('The convert_to_pdf_action cannot be None.')
