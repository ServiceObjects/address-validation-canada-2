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
//        Address
//        Address2
//        Municipality
//        PostalCode
//        Province
//        Language
//        TimeoutSeconds
//        LicenseKey
//        IsLive

using address_validation_canada_2_dot_net.REST;

ValidateCanadianAddressV2Client.ValidateCanadianAddressV2Input validateCanadianAddressV2Input = new(
    Address: "50 Coach Hill Dr",
    Address2: "",
    Municipality: "Kitchener",
    Province: "Ont",
    PostalCode: "N2E 1P4",
    Language: "English",
    LicenseKey: "YOUR LICENSE KEY",
    IsLive: true,
    TimeoutSeconds: 15
);

// 2. Call the sync Invoke() method.
AVCA2Response response = ValidateCanadianAddressV2Client.Invoke(validateCanadianAddressV2Input);

// 3. Inspect results.
if (response.Error is null)
{
    Console.WriteLine("\r\n* Address Info *\r\n");
    if (response.CanadianAddressInfoV2 != null)
    {
        CanadianAddressInfoV2 addressInfo = response.CanadianAddressInfoV2;
        Console.WriteLine($"Address                : {addressInfo.Address}");
        Console.WriteLine($"Address2               : {addressInfo.Address2}");
        Console.WriteLine($"Municipality           : {addressInfo.Municipality}");
        Console.WriteLine($"Province               : {addressInfo.Province}");
        Console.WriteLine($"PostalCode             : {addressInfo.PostalCode}");
        Console.WriteLine($"TimeZone               : {addressInfo.TimeZone}");
        Console.WriteLine($"AddressNumberFragment  : {addressInfo.AddressNumberFragment}");
        Console.WriteLine($"StreetNameFragment     : {addressInfo.StreetNameFragment}");
        Console.WriteLine($"StreetTypeFragment     : {addressInfo.StreetTypeFragment}");
        Console.WriteLine($"DirectionalCodeFragment: {addressInfo.DirectionalCodeFragment}");
        Console.WriteLine($"UnitTypeFragment       : {addressInfo.UnitTypeFragment}");
        Console.WriteLine($"UnitNumberFragment     : {addressInfo.UnitNumberFragment}");
        Console.WriteLine($"IsPOBox                : {addressInfo.IsPOBox}");
        Console.WriteLine($"BoxNumberFragment      : {addressInfo.BoxNumberFragment}");
        Console.WriteLine($"StationInfo            : {addressInfo.StationInfo}");
        Console.WriteLine($"DeliveryMode           : {addressInfo.DeliveryMode}");
        Console.WriteLine($"DeliveryInstallation   : {addressInfo.DeliveryInstallation}");
        Console.WriteLine($"Corrections            : {addressInfo.Corrections}");
        Console.WriteLine($"CorrectionsDescriptions: {addressInfo.CorrectionsDescriptions}");
    }
    else
    {
        Console.WriteLine("No address info found.");
    }
}
else
{
    Console.WriteLine("\r\n* Error *\r\n");
    Console.WriteLine($"Error Type    : {response.Error.Type}");
    Console.WriteLine($"Error TypeCode: {response.Error.TypeCode}");
    Console.WriteLine($"Error Desc    : {response.Error.Desc}");
    Console.WriteLine($"Error DescCode: {response.Error.DescCode}");
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
//        Municipality
//        PostalCode
//        Province
//        TimeoutSeconds
//        LicenseKey
//        IsLive

using address_validation_canada_2_dot_net.REST;

ValidateCanadianMunicipalityProvinceClient.ValidateCanadianMunicipalityProvinceInput validateCanadianMunicipalityProvinceInput = new(
    Municipality: "Bowen Island",
    Province: "BC",
    PostalCode: "V0N 1G2",
    LicenseKey: licenseKey,
    IsLive: isLive,
    TimeoutSeconds: 15
);

// 2. Call the sync Invoke() method.
 AVCA2Response response = ValidateCanadianMunicipalityProvinceClient.Invoke(validateCanadianMunicipalityProvinceInput);

// 3. Inspect results.
if (response.Error is null)
{
    Console.WriteLine("\r\n* Address Info *\r\n");
    if (response.CanadianAddressInfo != null)
    {
        CanadianAddressInfo addressInfo = response.CanadianAddressInfo;
        Console.WriteLine($"Address                : {addressInfo.Address}");
        Console.WriteLine($"Address2               : {addressInfo.Address2}");
        Console.WriteLine($"Municipality           : {addressInfo.Municipality}");
        Console.WriteLine($"Province               : {addressInfo.Province}");
        Console.WriteLine($"PostalCode             : {addressInfo.PostalCode}");
        Console.WriteLine($"TimeZone               : {addressInfo.TimeZone}");
        Console.WriteLine($"AddressNumberFragment  : {addressInfo.AddressNumberFragment}");
        Console.WriteLine($"StreetNameFragment     : {addressInfo.StreetNameFragment}");
        Console.WriteLine($"StreetTypeFragment     : {addressInfo.StreetTypeFragment}");
        Console.WriteLine($"DirectionalCodeFragment: {addressInfo.DirectionalCodeFragment}");
        Console.WriteLine($"UnitTypeFragment       : {addressInfo.UnitTypeFragment}");
        Console.WriteLine($"UnitNumberFragment     : {addressInfo.UnitNumberFragment}");
        Console.WriteLine($"IsPOBox                : {addressInfo.IsPOBox}");
        Console.WriteLine($"BoxNumberFragment      : {addressInfo.BoxNumberFragment}");
        Console.WriteLine($"StationInfo            : {addressInfo.StationInfo}");
        Console.WriteLine($"DeliveryMode           : {addressInfo.DeliveryMode}");
        Console.WriteLine($"DeliveryInstallation   : {addressInfo.DeliveryInstallation}");
    }
    else
    {
        Console.WriteLine("No address info found.");
    }
}
else
{
    Console.WriteLine("\r\n* Error *\r\n");
    Console.WriteLine($"Error Type    : {response.Error.Type}");
    Console.WriteLine($"Error TypeCode: {response.Error.TypeCode}");
    Console.WriteLine($"Error Desc    : {response.Error.Desc}");
    Console.WriteLine($"Error DescCode: {response.Error.DescCode}");
}
```