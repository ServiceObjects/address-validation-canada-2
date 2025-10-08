using address_validation_canada_2_dot_net.REST;
using address_validation_canada_2_dot_net_examples;

//Your license key from Service Objects.
//Trial license keys will only work on the
//trail environments and production license
//keys will only work on production environments.
string LicenseKey = "LICENSE KEY";

bool IsProductionKey = true;

//Address Validation – Canada 2 - ValidateCanadianAddressV2 - REST SDK
ValidateCanadianAddressV2RestSdkExample.Go(LicenseKey, IsProductionKey);

//Address Validation – Canada 2 - ValidateCanadianAddressV2 - SOAP SDK
ValidateCanadianAddressV2SoapSdkExample.Go(LicenseKey, IsProductionKey);

//Address Validation – Canada 2 - ValidateCanadianMunicipalityProvince - REST SDK
ValidateCanadianMunicipalityProvinceRestSdkExample.Go(LicenseKey, IsProductionKey);

//Address Validation – Canada 2 - ValidateCanadianMunicipalityProvince - SOAP SDK
ValidateCanadianMunicipalityProvinceSoapSdkExample.Go(LicenseKey, IsProductionKey);
