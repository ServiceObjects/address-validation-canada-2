![Service Objects Logo](https://www.serviceobjects.com/wp-content/uploads/2021/05/SO-Logo-with-TM.gif "Service Objects Logo")

# AVCA2 - Address Validation Canada 2

DOTS Address Validation Canada 2 (AVCA2) is a publicly available XML web service that provides parsed and corrected information about a physical Canadian address. The service provides corrected information such as the correct street location and postal code as well as address fragments and locational metadata.

AVCA2 can provide instant address verification and correction to websites or enhancement to contact lists. However, the output from AVCA2 must be considered carefully before the existence or non-existence of an address is decided.

## [Service Objects Website](https://serviceobjects.com)
## [Developer Guide/Documentation](https://www.serviceobjects.com/docs/)

# AVCA2 - ValidateCanadianAddressV2

This operation performs basic checks on user-supplied inputs; Address1, Address2, Municipality, Province or Postal Code and returns verified Address, Municipality, Province, and Postal Code in Canadian address recommended format which is uppercased. There is also a method to return proper cased addresses by appending “-Proper” to the language parameter (e.g Language=EN-Proper). This operation also returns the time zone and a check if the supplied location is a P.O. Box, General Delivery, or Rural Route. This operation requires either a Postal Code or both Municipality and Province.  Providing all inputs is recommended because it helps the validation proceed if some of the elements are malformed.   

## [GetBestMatches Developer Guide/Documentation](https://www.serviceobjects.com/docs/dots-address-validation-us-3/av3-operations/av3-getbestmatches-recommended/)

## ValidateCanadianAddressV2 Request URLs (Query String Parameters)

>[!CAUTION]
>### *Important - Use query string parameters for all inputs.  Do not use path parameters since it will lead to errors due to optional parameters and special character issues.*


### JSON
#### Trial

https://trial.serviceobjects.com/AVCA2/api.svc/ValidateCanadianAddressV2?Address=50+Coach+Hill+Dr&Address2=&Municipality=Kitchener&Province=Ont&PostalCode=N2E+1P4&Language=English&Format=json&LicenseKey={LicenseKey}


#### Production

https://sws.serviceobjects.com/AVCA2/api.svc/ValidateCanadianAddressV2?Address=50+Coach+Hill+Dr&Address2=&Municipality=Kitchener&Province=Ont&PostalCode=N2E+1P4&Language=English&Format=json&LicenseKey={LicenseKey}

#### Production Backup

https://swsbackup.serviceobjects.com/AVCA2/api.svc/ValidateCanadianAddressV2?Address=50+Coach+Hill+Dr&Address2=&Municipality=Kitchener&Province=Ont&PostalCode=N2E+1P4&Language=English&Format=json&LicenseKey={LicenseKey}

### XML
#### Trial

https://trial.serviceobjects.com/AVCA2/api.svc/ValidateCanadianAddressV2?Address=50+Coach+Hill+Dr&Address2=&Municipality=Kitchener&Province=Ont&PostalCode=N2E+1P4&Language=English&LicenseKey={LicenseKey}

#### Production

https://sws.serviceobjects.com/AVCA2/api.svc/ValidateCanadianAddressV2?Address=50+Coach+Hill+Dr&Address2=&Municipality=Kitchener&Province=Ont&PostalCode=N2E+1P4&Language=English&LicenseKey={LicenseKey}

#### Production Backup

https://swsbackup.serviceobjects.com/AVCA2/api.svc/ValidateCanadianAddressV2?Address=50+Coach+Hill+Dr&Address2=&Municipality=Kitchener&Province=Ont&PostalCode=N2E+1P4&Language=English&LicenseKey={LicenseKey}

# AV3 - ValidateCanadianMunicipalityProvince

This operation performs basic checks on user-supplied inputs; Municipality, Province, or Postal Code and returns verified Municipality, Province, and Postal Code. This operation also returns the time zone and a check if the supplied location is a P.O. Box, General Delivery, or Rural Route. This operation requires either a Postal Code or both Municipality and Province. Providing all inputs is recommended because it helps the validation proceed if some of the elements are malformed.

## [ValidateCanadianMunicipalityProvince Developer Guide/Documentation](https://www.serviceobjects.com/docs/dots-address-validation-canada-2/avca2-operations/avca2-validatecanadianmunicipalityprovince/)

## ValidateCanadianMunicipalityProvince Request URLs (Query String Parameters)

>[!CAUTION]
>#### *Important - Use query string parameters for all inputs.  Do not use path parameters since it will lead to errors due to optional parameters and special character issues.*

### JSON
#### Trial

https://trial.serviceobjects.com/AVCA2/api.svc/ValidateCanadianMunicipalityProvince?PostalCode=V0N%201G2&Province=BC&Municipality=Bowen%20Island&format=json&LicenseKey={LicenseKey}

#### Production

https://sws.serviceobjects.com/AVCA2/api.svc/ValidateCanadianMunicipalityProvince?PostalCode=V0N%201G2&Province=BC&Municipality=Bowen%20Island&format=json&LicenseKey={LicenseKey}

#### Production Backup

https://swsbackup.serviceobjects.com/AVCA2/api.svc/ValidateCanadianMunicipalityProvince?PostalCode=V0N%201G2&Province=BC&Municipality=Bowen%20Island&format=json&LicenseKey={LicenseKey}

### XML
#### Trial

https://trial.serviceobjects.com/AVCA2/api.svc/ValidateCanadianMunicipalityProvince?PostalCode=V0N%201G2&Province=BC&Municipality=Bowen%20Island&format=xml&LicenseKey={LicenseKey}

#### Production

https://sws.serviceobjects.com/AVCA2/api.svc/ValidateCanadianMunicipalityProvince?PostalCode=V0N%201G2&Province=BC&Municipality=Bowen%20Island&format=xml&LicenseKey={LicenseKey}

#### Production Backup

https://swsbackup.serviceobjects.com/AVCA2/api.svc/ValidateCanadianMunicipalityProvince?PostalCode=V0N%201G2&Province=BC&Municipality=Bowen%20Island&format=xml&LicenseKey={LicenseKey}
