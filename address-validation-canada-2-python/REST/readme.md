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

from validate_canadian_address_v2_rest import validate_canadian_address_v2

address = "50 Coach Hill Dr"
address2 = ""
municipality = "Kitchener"
province = "Ont"
postal_code = "N2E 1P4"
language = "English"
is_live = True
license_key = "YOUR LICENSE KEY"


# 2. Call the method.
response = validate_canadian_address_v2(address, address2, municipality, province, postal_code, language, license_key, is_live)

# 3. Inspect results.
print("\r\n* Address Info *\r\n")
if response and not response.Error:
    if response.CanadianAddressInfoV2:
        address_info = response.CanadianAddressInfoV2
        print(f"Address              : {address_info.Address}")
        print(f"Address2             : {address_info.Address2}")
        print(f"Municipality         : {address_info.Municipality}")
        print(f"Province             : {address_info.Province}")
        print(f"Postal Code          : {address_info.PostalCode}")
        print(f"Time Zone            : {address_info.TimeZone}")
        print(f"Address Number       : {address_info.AddressNumberFragment}")
        print(f"Street Name          : {address_info.StreetNameFragment}")
        print(f"Street Type          : {address_info.StreetTypeFragment}")
        print(f"Directional Code     : {address_info.DirectionalCodeFragment}")
        print(f"Unit Type            : {address_info.UnitTypeFragment}")
        print(f"Unit Number          : {address_info.UnitNumberFragment}")
        print(f"Is PO Box            : {address_info.IsPOBox}")
        print(f"Box Number           : {address_info.BoxNumberFragment}")
        print(f"Station Info         : {address_info.StationInfo}")
        print(f"Delivery Mode        : {address_info.DeliveryMode}")
        print(f"Delivery Installation: {address_info.DeliveryInstallation}")
        print(f"Corrections          : {address_info.Corrections}")
        print(f"Corrections Desc     : {address_info.CorrectionsDescriptions}")
    else:
        print("No CanadianAddressInfoV2 found.")
else:
    print("No address info found.")

if response.Error:
    print("\r\n* Error *\r\n")
    print(f"Error Type     : {response.Error.Type}")
    print(f"Error Type Code: {response.Error.TypeCode}")
    print(f"Error Desc     : {response.Error.Desc}")
    print(f"Error Desc Code: {response.Error.DescCode}")
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

from validate_canadian_municipality_province_rest import validate_canadian_municipality_province

municipality = "Bowen Island"
province = "BC"
postal_code = "V0N 1G2"
is_live = True
license_key = "YOUR LICENSE KEY"

# 2. Call the method.
response = validate_canadian_municipality_province(municipality, province, postal_code, license_key, is_live)

# 3. Inspect results.
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
```