
namespace address_validation_canada_2_dot_net.REST
{
    public class ValidateCanadianAddressV2RestSdkExample
    {
        public static void Go(string licenseKey, bool isLive)
        {
            Console.WriteLine("\r\n--------------------------------------------");
            Console.WriteLine("AVCA2 - ValidateCanadianAddressV2 - REST SDK");
            Console.WriteLine("--------------------------------------------");

            ValidateCanadianAddressV2Client.ValidateCanadianAddressV2Input validateCanadianAddressV2Input = new(
                Address: "50 Coach Hill Dr",
                Address2: "",
                Municipality: "Kitchener",
                Province: "Ont",
                PostalCode: "N2E 1P4",
                Language: "English",
                LicenseKey: licenseKey,
                IsLive: isLive,
                TimeoutSeconds: 15
            );

            Console.WriteLine("\r\n* Input *\r\n");
            Console.WriteLine($"Address     : {validateCanadianAddressV2Input.Address}");
            Console.WriteLine($"Address2    : {validateCanadianAddressV2Input.Address2}");
            Console.WriteLine($"Municipality: {validateCanadianAddressV2Input.Municipality}");
            Console.WriteLine($"Province    : {validateCanadianAddressV2Input.Province}");
            Console.WriteLine($"PostalCode  : {validateCanadianAddressV2Input.PostalCode}");
            Console.WriteLine($"Language    : {validateCanadianAddressV2Input.Language}");
            Console.WriteLine($"License Key : {validateCanadianAddressV2Input.LicenseKey}");
            Console.WriteLine($"Is Live     : {validateCanadianAddressV2Input.IsLive}");

            AVCA2Response response = ValidateCanadianAddressV2Client.Invoke(validateCanadianAddressV2Input);
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
        }
    }
}