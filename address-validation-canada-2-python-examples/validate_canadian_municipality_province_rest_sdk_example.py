import sys
import os

sys.path.insert(0, os.path.abspath("../address-validation-canada-2-python/REST"))

from validate_canadian_municipality_province_rest import validate_canadian_municipality_province

def validate_canadian_municipality_province_rest_sdk_go(is_live: bool, license_key: str) -> None:
    print("\r\n-------------------------------------------------------")
    print("AVCA2 - ValidateCanadianMunicipalityProvince - REST SDK")
    print("-------------------------------------------------------")

    municipality = "Bowen Island"
    province = "BC"
    postal_code = "V0N 1G2"

    print("\r\n* Input *\r\n")
    print(f"Municipality: {municipality}")
    print(f"Province    : {province}")
    print(f"Postal Code : {postal_code}")
    print(f"License Key : {license_key}")
    print(f"Is Live     : {is_live}")

    try:
        response = validate_canadian_municipality_province(
            municipality, province, postal_code, license_key, is_live
        )

        print("\r\n* Address Info *\r\n")
        if response and not response.Error:
            if response.CanadianAddressInfo:
                address_info = response.CanadianAddressInfo
                print(f"Address              : {address_info.Address }")
                print(f"Address2             : {address_info.Address2 }")
                print(f"Municipality         : {address_info.Municipality}")
                print(f"Province             : {address_info.Province}")
                print(f"Postal Code          : {address_info.PostalCode}")
                print(f"Time Zone            : {address_info.TimeZone}")
                print(f"Address Number       : {address_info.AddressNumberFragment }")
                print(f"Street Name          : {address_info.StreetNameFragment }")
                print(f"Street Type          : {address_info.StreetTypeFragment }")
                print(f"Directional Code     : {address_info.DirectionalCodeFragment }")
                print(f"Unit Type            : {address_info.UnitTypeFragment }")
                print(f"Unit Number          : {address_info.UnitNumberFragment }")
                print(f"Is PO Box            : {address_info.IsPOBox}")
                print(f"Box Number           : {address_info.BoxNumberFragment }")
                print(f"Station Info         : {address_info.StationInfo }")
                print(f"Delivery Mode        : {address_info.DeliveryMode}")
                print(f"Delivery Installation: {address_info.DeliveryInstallation}")
            else:
                print("No CanadianAddressInfo found.")
        else:
            print("No address info found.")

        if response.Error:
            print("\r\n* Error *\r\n")
            print(f"Error Type      : {response.Error.Type}")
            print(f"Error Type Code : {response.Error.TypeCode}")
            print(f"Error Desc      : {response.Error.Desc}")
            print(f"Error Desc Code : {response.Error.DescCode}")

    except Exception as e:
        print("\r\n* Error *\r\n")
        print(f"Error Message: {str(e)}")