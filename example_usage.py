from client import OpenapiToMockServiceSynthesizerClient

def main():
    client = OpenapiToMockServiceSynthesizerClient()
    res = client.synthesize_mock_handlers('Ecommerce API', 12)
    print('Mock Service Synthesizer: ' + res['mock_service_id'] + ' (' + res['openapi_spec_title'] + ')')
    print('Handlers: ' + str(res['mock_handlers_generated']) + ' | MSW Worker Ready: ' + str(res['msw_browser_worker_ready']))
    print('Bundle URL: ' + res['offline_mock_bundle_url'])

if __name__ == '__main__':
    main()
