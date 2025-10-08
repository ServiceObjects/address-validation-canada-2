import { ValidateCanadianMunicipalityProvinceClient } from '../address-validation-canada-2-nodejs/REST/validate_canadian_municipality_province_rest.js';

async function ValidateCanadianMunicipalityProvinceRestGo(licenseKey, isLive) {
    console.log("\n-------------------------------------------------------");
    console.log("AVCA2 - ValidateCanadianMunicipalityProvince - REST SDK");
    console.log("-------------------------------------------------------");

    const municipality = "Bowen Island";
    const province = "BC";
    const postalCode = "V0N 1G2";
    const timeoutSeconds = 15;

    console.log("\n* Input *\n");
    console.log(`Municipality   : ${municipality}`);
    console.log(`Province       : ${province}`);
    console.log(`Postal Code    : ${postalCode}`);
    console.log(`License Key    : ${licenseKey}`);
    console.log(`Is Live        : ${isLive}`);
    console.log(`Timeout Seconds: ${timeoutSeconds}`);

    try {
        const response = await ValidateCanadianMunicipalityProvinceClient.invoke(
            municipality,
            province,
            postalCode,
            licenseKey,
            isLive,
            timeoutSeconds
        );

        if (response.Error) {
            console.log("\n* Error *\n");
            console.log(`Error Type     : ${response.Error.Type}`);
            console.log(`Error Type Code: ${response.Error.TypeCode}`);
            console.log(`Error Desc     : ${response.Error.Desc}`);
            console.log(`Error Desc Code: ${response.Error.DescCode}`);
            return;
        }

        console.log("\n* Address Info *\n");
        if (response) {
            if (response.CanadianAddressInfo) {
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
            } else {
                console.log("No CanadianAddressInfo found.");
            }
        } else {
            console.log("No address info found.");
        }
    } catch (e) {
        console.log("\n* Error *\n");
        console.log(`Error Message: ${e.message}`);
    }
}

export { ValidateCanadianMunicipalityProvinceRestGo };