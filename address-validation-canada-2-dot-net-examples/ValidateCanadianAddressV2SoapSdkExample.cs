using System;
using AVCA2Reference;
using address_validation_canada_2_dot_net.SOAP;

namespace address_validation_canada_2_dot_net_examples
{
    internal class ValidateCanadianAddressV2SoapSdkExample
    {
        public static void Go(string licenseKey, bool isLive)
        {
            Console.WriteLine("\r\n--------------------------------------------");
            Console.WriteLine("AVCA2 - ValidateCanadianAddressV2 - SOAP SDK");
            Console.WriteLine("--------------------------------------------");

            string Address = "50 Coach Hill Dr";
            string Address2 = "";
            string Municipality = "Kitchener";
            string Province = "Ont";
            string PostalCode = "N2E 1P4";
            string Language = "English";

            Console.WriteLine("\r\n* Input *\r\n");
            Console.WriteLine($"Address     : {Address}");
            Console.WriteLine($"Address2    : {Address2}");
            Console.WriteLine($"Municipality: {Municipality}");
            Console.WriteLine($"Province    : {Province}");
            Console.WriteLine($"PostalCode  : {PostalCode}");
            Console.WriteLine($"Language    : {Language}");
            Console.WriteLine($"License Key : {licenseKey}");
            Console.WriteLine($"Is Live     : {isLive}");

            var avca2 = new ValidateCanadianAddressV2Validation(isLive);
            CanadianAddressResponseV2 response = avca2.ValidateCanadianAddressV2(
                Address, Address2, Municipality, Province, PostalCode, Language, licenseKey).Result;

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