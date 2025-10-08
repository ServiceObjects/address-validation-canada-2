import { ValidateCanadianAddressV2Soap } from '../address-validation-canada-2-nodejs/SOAP/validate_canadian_address_v2_soap.js';

async function ValidateCanadianAddressV2SoapGo(licenseKey, isLive) {
    console.log("\n--------------------------------------------");
    console.log("AVCA2 - ValidateCanadianAddressV2 - SOAP SDK");
    console.log("--------------------------------------------");

    const address = "50 Coach Hill Dr";
    const address2 = "";
    const municipality = "Kitchener";
    const province = "Ont";
    const postalCode = "N2E 1P4";
    const language = "English";
    const timeoutSeconds = 15;

    console.log("\n* Input *\n");
    console.log(`Address        : ${address}`);
    console.log(`Address2       : ${address2}`);
    console.log(`Municipality   : ${municipality}`);
    console.log(`Province       : ${province}`);
    console.log(`Postal Code    : ${postalCode}`);
    console.log(`Language       : ${language}`);
    console.log(`License Key    : ${licenseKey}`);
    console.log(`Is Live        : ${isLive}`);
    console.log(`Timeout Seconds: ${timeoutSeconds}`);

    try {
        const avca2 = new ValidateCanadianAddressV2Soap(
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
        const response = await avca2.invokeAsync();

        if (response.Error) {
            console.log("\n* Error *\n");
            console.log(`Error Type      : ${response.Error.Type}`);
            console.log(`Error Type Code : ${response.Error.TypeCode}`);
            console.log(`Error Desc      : ${response.Error.Desc}`);
            console.log(`Error Desc Code : ${response.Error.DescCode}`);
            return;
        }

        console.log("\n* Address Info *\n");
        if (response) {
            if (response.CanadianAddressInfoV2) {
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
            } else {
                console.log("No CanadianAddressInfoV2 found.");
            }
        } else {
            console.log("No address info found.");
        }
    } catch (e) {
        console.log("\n* Error *\n");
        console.log(`Error Message: ${e.message}`);
    }
}

export { ValidateCanadianAddressV2SoapGo };