from validate_canadian_address_v2_rest_sdk_example import validate_canadian_address_v2_rest_sdk_go
from validate_canadian_address_v2_soap_sdk_example import validate_canadian_address_v2_soap_sdk_go
from validate_canadian_municipality_province_rest_sdk_example import validate_canadian_municipality_province_rest_sdk_go
from validate_canadian_municipality_province_soap_sdk_example import validate_canadian_municipality_province_soap_sdk_go

if __name__ =="__main__":

    # Your license key from Service Objects.  
    # Trial license keys will only work on the trial environments and production  
    # license keys will only work on production environments.
    #   
    license_key = "LICENSE KEY"  
    is_live = True

    # Address Validation – Canada 2 - ValidateCanadianAddressV2 - REST SDK
    validate_canadian_address_v2_rest_sdk_go(is_live, license_key)

    # Address Validation – Canada 2 - ValidateCanadianAddressV2 - SOAP SDK
    validate_canadian_address_v2_soap_sdk_go(is_live, license_key)

    # Address Validation – Canada 2 - ValidateCanadianMunicipalityProvince - REST SDK
    validate_canadian_municipality_province_rest_sdk_go(is_live, license_key)

    # Address Validation – Canada 2 - ValidateCanadianMunicipalityProvince - SOAP SDK
    validate_canadian_municipality_province_soap_sdk_go(is_live, license_key)
