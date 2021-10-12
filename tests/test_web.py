from mamba.web.zillow import ZillowRequest


def test_zillow_request():
    zillow = ZillowRequest(2769, 'Brands Hatch Court', 'Henderson', 89052)