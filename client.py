class OpenapiToMockServiceSynthesizerClient:
    def synthesize_mock_handlers(self, openapi_spec_title='Storefront API v1', endpoints_count=8):
        return {
            'mock_service_id': 'mck_syn_5519',
            'openapi_spec_title': openapi_spec_title,
            'mock_handlers_generated': endpoints_count,
            'faker_fixtures_populated': True,
            'msw_browser_worker_ready': True,
            'offline_mock_bundle_url': 'https://lovable.mock.genpark.ai/bundles/5519.js'
        }
