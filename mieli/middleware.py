class MieliMiddleware(object):
    def process_request(self, request):
        request.organization = request.site.organization_set.get()
        return None
