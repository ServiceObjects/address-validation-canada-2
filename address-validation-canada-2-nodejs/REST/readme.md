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
// 1. Build the input
//
//  Fields:
//        address
//        address2
//        municipality
//        postalCode
//        province
//        language
//        timeoutSeconds
//        licenseKey
//        isLive

import { ValidateCanadianAddressV2Client } from '../address-validation-canada-2-nodejs/REST/validate_canadian_address_v2_rest.js';

const address = "50 Coach Hill Dr";
const address2 = "";
const municipality = "Kitchener";
const province = "Ont";
const postalCode = "N2E 1P4";
const language = "English";
const timeoutSeconds = 15;
const isLive = true;
const licenseKey = "YOUR LICENSE KEY";

// 2. Call the sync Invoke() method.
const response = await ValidateCanadianAddressV2Client.invoke(
    address,
    address2,
    municipality,
    province,
    postalCode,
    language,
    licenseKey,
    isLive,
    timeoutSeconds
);

// 3. Inspect results.
if (response.Error) 
{
    console.log("\n* Error *\n");
    console.log(`Error Type     : ${response.Error.Type}`);
    console.log(`Error Type Code: ${response.Error.TypeCode}`);
    console.log(`Error Desc     : ${response.Error.Desc}`);
    console.log(`Error Desc Code: ${response.Error.DescCode}`);
    return;
}

console.log("\n* Address Info *\n");
if (response) 
{
    if (response.CanadianAddressInfoV2) 
    {
        console.log(`Address              : ${response.CanadianAddressInfoV2.Address}`);
        console.log(`Address2             : ${response.CanadianAddressInfoV2.Address2}`);
        console.log(`Municipality         : ${response.CanadianAddressInfoV2.Municipality}`);
        console.log(`Province             : ${response.CanadianAddressInfoV2.Province}`);
        console.log(`Postal Code          : ${response.CanadianAddressInfoV2.PostalCode}`);
        console.log(`Time Zone            : ${response.CanadianAddressInfoV2.TimeZone}`);
        console.log(`Address Number       : ${response.CanadianAddressInfoV2.AddressNumberFragment}`);
        console.log(`Street Name          : ${response.CanadianAddressInfoV2.StreetNameFragment}`);
        console.log(`Street Type          : ${response.CanadianAddressInfoV2.StreetTypeFragment}`);
        console.log(`Directional Code     : ${response.CanadianAddressInfoV2.DirectionalCodeFragment}`);
        console.log(`Unit Type            : ${response.CanadianAddressInfoV2.UnitTypeFragment}`);
        console.log(`Unit Number          : ${response.CanadianAddressInfoV2.UnitNumberFragment}`);
        console.log(`Is PO Box            : ${response.CanadianAddressInfoV2.IsPOBox}`);
        console.log(`Box Number           : ${response.CanadianAddressInfoV2.BoxNumberFragment}`);
        console.log(`Station Info         : ${response.CanadianAddressInfoV2.StationInfo}`);
        console.log(`Delivery Mode        : ${response.CanadianAddressInfoV2.DeliveryMode}`);
        console.log(`Delivery Installation: ${response.CanadianAddressInfoV2.DeliveryInstallation}`);
        console.log(`Corrections          : ${response.CanadianAddressInfoV2.Corrections}`);
        console.log(`Corrections Desc     : ${response.CanadianAddressInfoV2.CorrectionsDescriptions}`);
    } 
    else
    {
        console.log("No CanadianAddressInfoV2 found.");
    }
} 
else
{
    console.log("No address info found.");
}
```
# AVCA2 - ValidateCanadianMunicipalityProvince

This operation performs basic checks on user-supplied inputs; Municipality, Province, or Postal Code and returns verified Municipality, Province, and Postal Code. 

This operation also returns the time zone and a check if the supplied location is a P.O. Box, General Delivery, or Rural Route. 

This operation requires either a Postal Code or both Municipality and Province. Providing all inputs is recommended because it helps the validation proceed if some of the elements are malformed. 

### [ValidateCanadianMunicipalityProvince Developer Guide/Documentation](https://www.serviceobjects.com/docs/dots-address-validation-canada-2/avca2-operations/avca2-validatecanadianmunicipalityprovince/)

## Library Usage

```
// 1. Build the input
//
//  Fields:
//        municipality
//        postalCode
//        province
//        timeoutSeconds
//        licenseKey
//        isLive

import { ValidateCanadianMunicipalityProvinceClient } from '../address-validation-canada-2-nodejs/REST/validate_canadian_municipality_province_rest.js';

const municipality = "Bowen Island";
const province = "BC";
const postalCode = "V0N 1G2";
const timeoutSeconds = 15;
const isLive = true;
const licenseKey = "YOUR LICENSE KEY";

// 2. Call the sync Invoke() method.
const response = await ValidateCanadianMunicipalityProvinceClient.invoke(
    municipality,
    province,
    postalCode,
    licenseKey,
    isLive,
    timeoutSeconds
);

// 3. Inspect results.
if (response.Error) 
{
    console.log("\n* Error *\n");
    console.log(`Error Type     : ${response.Error.Type}`);
    console.log(`Error Type Code: ${response.Error.TypeCode}`);
    console.log(`Error Desc     : ${response.Error.Desc}`);
    console.log(`Error Desc Code: ${response.Error.DescCode}`);
    return;
}

console.log("\n* Address Info *\n");
if (response) 
{
    if (response.CanadianAddressInfo)
    {
        console.log(`Address              : ${response.CanadianAddressInfo.Address}`);
        console.log(`Address2             : ${response.CanadianAddressInfo.Address2}`);
        console.log(`Municipality         : ${response.CanadianAddressInfo.Municipality}`);
        console.log(`Province             : ${response.CanadianAddressInfo.Province}`);
        console.log(`Postal Code          : ${response.CanadianAddressInfo.PostalCode}`);
        console.log(`Time Zone            : ${response.CanadianAddressInfo.TimeZone}`);
        console.log(`Address Number       : ${response.CanadianAddressInfo.AddressNumberFragment}`);
        console.log(`Street Name          : ${response.CanadianAddressInfo.StreetNameFragment}`);
        console.log(`Street Type          : ${response.CanadianAddressInfo.StreetTypeFragment}`);
        console.log(`Directional Code     : ${response.CanadianAddressInfo.DirectionalCodeFragment}`);
        console.log(`Unit Type            : ${response.CanadianAddressInfo.UnitTypeFragment}`);
        console.log(`Unit Number          : ${response.CanadianAddressInfo.UnitNumberFragment}`);
        console.log(`Is PO Box            : ${response.CanadianAddressInfo.IsPOBox}`);
        console.log(`Box Number           : ${response.CanadianAddressInfo.BoxNumberFragment}`);
        console.log(`Station Info         : ${response.CanadianAddressInfo.StationInfo}`);
        console.log(`Delivery Mode        : ${response.CanadianAddressInfo.DeliveryMode}`);
        console.log(`Delivery Installation: ${response.CanadianAddressInfo.DeliveryInstallation}`);
    }
    else
    {
        console.log("No CanadianAddressInfo found.");
    }
} 
else 
{
    console.log("No address info found.");
}
```