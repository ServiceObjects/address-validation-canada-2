import {ValidateCanadianAddressV2RestGo } from './validate_canadian_address_v2_rest_sdk_example.js'; 
import { ValidateCanadianAddressV2SoapGo } from './validate_canadian_address_v2_soap_sdk_example.js';
import { ValidateCanadianMunicipalityProvinceRestGo } from './validate_canadian_municipality_province_rest_sdk_example.js';
import { ValidateCanadianMunicipalityProvinceSoapGo } from './validate_canadian_municipality_province_soap_sdk_example.js';

export async function main() {
    //Your license key from Service Objects.
    //Trial license keys will only work on the
    //trail environments and production license
    //keys will only work on production environments.
    const licenseKey = "LICENSE KEY";
    const isLive = true;

    // Address Validation – Canada 2 - ValidateCanadianAddressV2 - REST SDK
    await ValidateCanadianAddressV2RestGo(licenseKey, isLive);

    // Address Validation – Canada 2 - ValidateCanadianAddressV2 - SOAP SDK
    await ValidateCanadianAddressV2SoapGo(licenseKey, isLive);

    // Address Validation – Canada 2 - ValidateCanadianMunicipalityProvince - REST SDK
    await ValidateCanadianMunicipalityProvinceRestGo(licenseKey, isLive);

    // Address Validation – Canada 2 - ValidateCanadianMunicipalityProvince - SOAP SDK
    await ValidateCanadianMunicipalityProvinceSoapGo(licenseKey, isLive);

}
main().catch((error) => {
    console.error("An error occurred:", error);
    process.exit(1);
});