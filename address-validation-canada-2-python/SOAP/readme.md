![Service Objects Logo](https://www.serviceobjects.com/wp-content/uploads/2021/05/SO-Logo-with-TM.gif "Service Objects Logo")

# AVCA2 - Address Validation – Canada 2

DOTS Address Validation Canada 2 (AVCA2) is a publicly available XML web service that provides parsed and corrected information about a physical Canadian address. The service provides corrected information such as the correct street location and postal code as well as address fragments and locational metadata.

AVCA2 can provide instant address verification and correction to websites or enhancement to contact lists. However, the output from AVCA2 must be considered carefully before the existence or non-existence of an address is decided.

## [Service Objects Website](https://serviceobjects.com)

# AVCA2 - ValidateCanadianAddressV2

This operation performs basic checks on user-supplied inputs; Address1, Address2, Municipality, Province or Postal Code and returns verified Address, Municipality, Province, and Postal Code in Canadian address recommended format which is uppercased. There is also a method to return proper cased addresses by appending “-Proper” to the language parameter (e.g Language=EN-Proper). 

This operation also returns the time zone and a check if the supplied location is a P.O. Box, General Delivery, or Rural Route. This operation requires either a Postal Code or both Municipality and Province.  

Providing all inputs is recommended because it helps the validation proceed if some of the elements are malformed. 

### [ValidateCanadianAddressV2 Developer Guide/Documentation](https://www.serviceobjects.com/docs/dots-address-validation-canada-2/avca2-operations/avca2-validatecanadianaddressv2-recommended/)

## Library Usage

```
# 1. Build the input
#
#  Fields:
#        address
#        address2
#        municipality
#        postal_code
#        province
#        language
#        license_key
#        is_live
#        timeout_seconds

from validate_canadian_address_v2_soap import ValidateCanadianAddressV2Soap

address = "50 Coach Hill Dr"
address2 = ""
municipality = "Kitchener"
province = "Ont"
postal_code = "N2E 1P4"
language = "English"
timeout_seconds = 15
is_live = True
license_key = "YOUR LICENSE KEY"

# 2. Call the method.
service = ValidateCanadianAddressV2Soap(license_key, is_live, timeout_seconds * 1000)
response = service.validate_canadian_address_v2(address, address2, municipality, province, postal_code, language)

# 3. Inspect results.
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
```
# AVCA2 - ValidateCanadianMunicipalityProvince

This operation performs basic checks on user-supplied inputs; Municipality, Province, or Postal Code and returns verified Municipality, Province, and Postal Code. 

This operation also returns the time zone and a check if the supplied location is a P.O. Box, General Delivery, or Rural Route. 

This operation requires either a Postal Code or both Municipality and Province. Providing all inputs is recommended because it helps the validation proceed if some of the elements are malformed. 

### [ValidateCanadianMunicipalityProvince Developer Guide/Documentation](https://www.serviceobjects.com/docs/dots-address-validation-canada-2/avca2-operations/avca2-validatecanadianmunicipalityprovince/)

## Library Usage

```
# 1. Build the input
#
#  Fields:
#        municipality
#        postal_code
#        province
#        timeout_seconds
#        license_key
#        is_live

from validate_canadian_municipality_province_soap import ValidateCanadianMunicipalityProvinceSoap

municipality = "Bowen Island"
province = "BC"
postal_code = "V0N 1G2"
timeout_seconds = 15
is_live = True
license_key = "YOUR LICENSE KEY"

# 2. Call the method.
service = ValidateCanadianMunicipalityProvinceSoap(license_key, is_live, timeout_seconds * 1000)
response = service.validate_canadian_municipality_province(municipality, province, postal_code)

# 3. Inspect results.
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
```