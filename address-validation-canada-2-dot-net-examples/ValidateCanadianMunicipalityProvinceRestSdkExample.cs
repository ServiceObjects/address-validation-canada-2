using address_validation_canada_2_dot_net.REST;

namespace address_validation_canada_2_dot_net_examples
{
    public class ValidateCanadianMunicipalityProvinceRestSdkExample
    {
        public static void Go(string licenseKey, bool isLive)
        {
            Console.WriteLine("\r\n-------------------------------------------------------");
            Console.WriteLine("AVCA2 - ValidateCanadianMunicipalityProvince - REST SDK");
            Console.WriteLine("-------------------------------------------------------");

            ValidateCanadianMunicipalityProvinceClient.ValidateCanadianMunicipalityProvinceInput validateCanadianMunicipalityProvinceInput = new(
                Municipality: "Bowen Island",
                Province: "BC",
                PostalCode: "V0N 1G2",
                LicenseKey: licenseKey,
                IsLive: isLive,
                TimeoutSeconds: 15
            );

            Console.WriteLine("\r\n* Input *\r\n");
            Console.WriteLine($"Municipality: {validateCanadianMunicipalityProvinceInput.Municipality}");
            Console.WriteLine($"Province    : {validateCanadianMunicipalityProvinceInput.Province}");
            Console.WriteLine($"PostalCode  : {validateCanadianMunicipalityProvinceInput.PostalCode}");
            Console.WriteLine($"License Key : {validateCanadianMunicipalityProvinceInput.LicenseKey}");
            Console.WriteLine($"Is Live     : {validateCanadianMunicipalityProvinceInput.IsLive}");

            AVCA2Response response = ValidateCanadianMunicipalityProvinceClient.Invoke(validateCanadianMunicipalityProvinceInput);
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
        }
    }
}