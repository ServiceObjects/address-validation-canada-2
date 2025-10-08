import sys
import os

sys.path.insert(0, os.path.abspath("../address-validation-canada-2-python/SOAP"))

from validate_canadian_address_v2_soap import ValidateCanadianAddressV2Soap


def validate_canadian_address_v2_soap_sdk_go(is_live: bool, license_key: str) -> None:
    print("\r\n--------------------------------------------")
    print("AVCA2 - ValidateCanadianAddressV2 - SOAP SDK")
    print("--------------------------------------------")

    address = "50 Coach Hill Dr"
    address2 = ""
    municipality = "Kitchener"
    province = "Ont"
    postal_code = "N2E 1P4"
    language = "English"
    timeout_seconds = 15

    print("\r\n* Input *\r\n")
    print(f"Address        : {address}")
    print(f"Address2       : {address2}")
    print(f"Municipality   : {municipality}")
    print(f"Province       : {province}")
    print(f"Postal Code    : {postal_code}")
    print(f"Language       : {language}")
    print(f"License Key    : {license_key}")
    print(f"Is Live        : {is_live}")
    print(f"Timeout Seconds: {timeout_seconds}")

    try:
        service = ValidateCanadianAddressV2Soap(license_key, is_live, timeout_seconds * 1000)
        response = service.validate_canadian_address_v2(address, address2, municipality, province, postal_code, language)

        if not hasattr(response, 'Error') or not response.Error:
            print("\r\n* Address Info *\r\n")
            if hasattr(response, 'CanadianAddressInfoV2') and response.CanadianAddressInfoV2:
                address_info = response.CanadianAddressInfoV2
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
                print(f"Corrections          : {getattr(address_info, 'Corrections', None)}")
                print(f"Corrections Desc     : {getattr(address_info, 'CorrectionsDescriptions', None)}")
            else:
                print("No CanadianAddressInfoV2 found.")
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