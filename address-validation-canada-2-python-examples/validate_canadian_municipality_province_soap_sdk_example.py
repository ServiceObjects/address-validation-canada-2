import sys
import os

sys.path.insert(0, os.path.abspath("../address-validation-canada-2-python/SOAP"))

from validate_canadian_municipality_province_soap import ValidateCanadianMunicipalityProvinceSoap

def validate_canadian_municipality_province_soap_sdk_go(is_live: bool, license_key: str) -> None:
    print("\r\n-------------------------------------------------------")
    print("AVCA2 - ValidateCanadianMunicipalityProvince - SOAP SDK")
    print("-------------------------------------------------------")

    municipality = "Bowen Island"
    province = "BC"
    postal_code = "V0N 1G2"
    timeout_seconds = 15

    print("\r\n* Input *\r\n")
    print(f"Municipality   : {municipality}")
    print(f"Province       : {province}")
    print(f"Postal Code    : {postal_code}")
    print(f"License Key    : {license_key}")
    print(f"Is Live        : {is_live}")
    print(f"Timeout Seconds: {timeout_seconds}")

    try:
        service = ValidateCanadianMunicipalityProvinceSoap(license_key, is_live, timeout_seconds * 1000)
        response = service.validate_canadian_municipality_province(municipality, province, postal_code)

        if not hasattr(response, 'Error') or not response.Error:
            print("\r\n* Address Info *\r\n")
            if hasattr(response, 'CanadianAddressInfo') and response.CanadianAddressInfo:
                address_info = response.CanadianAddressInfo
                print(f"Address              : {getattr(address_info, 'Address', None)}")
                print(f"Address2             : {getattr(address_info, 'Address2', None)}")
                print(f"Municipality         : {getattr(address_info, 'Municipality', None)}")
                print(f"Province             : {getattr(address_info, 'Province', None)}")
                print(f"Postal Code          : {getattr(address_info, 'PostalCode', None)}")
                print(f"Time Zone            : {getattr(address_info, 'TimeZone', None)}")
                print(f"Address Number       : {getattr(address_info, 'AddressNumberFragment', None)}")
                print(f"Street Name          : {getattr(address_info, 'StreetNameFragment', None)}")
                print(f"Street Type          : {getattr(address_info, 'StreetTypeFragment', None)}")
                print(f"Directional Code     : {getattr(address_info, 'DirectionalCodeFragment', None)}")
                print(f"Unit Type            : {getattr(address_info, 'UnitTypeFragment', None)}")
                print(f"Unit Number          : {getattr(address_info, 'UnitNumberFragment', None)}")
                print(f"Is PO Box            : {getattr(address_info, 'IsPOBox', None)}")
                print(f"Box Number           : {getattr(address_info, 'BoxNumberFragment', None)}")
                print(f"Station Info         : {getattr(address_info, 'StationInfo', None)}")
                print(f"Delivery Mode        : {getattr(address_info, 'DeliveryMode', None)}")
                print(f"Delivery Installation: {getattr(address_info, 'DeliveryInstallation', None)}")
            else:
                print("No CanadianAddressInfo found.")
        else:
            print("No address info found.")

        if hasattr(response, 'Error') and response.Error:
            print("\r\n* Error *\r\n")
            print(f"Error Type      : {getattr(response.Error, 'Type', None)}")
            print(f"Error Type Code : {getattr(response.Error, 'TypeCode', None)}")
            print(f"Error Desc      : {getattr(response.Error, 'Desc', None)}")
            print(f"Error Desc Code : {getattr(response.Error, 'DescCode', None)}")

    except Exception as e:
        print("\r\n* Error *\r\n")
        print(f"Exception occurred: {str(e)}")