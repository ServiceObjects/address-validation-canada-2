using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace address_validation_canada_2_dot_net.REST
{
    public class AVCA2Response
    {
        public CanadianAddressInfoV2 CanadianAddressInfoV2 { get; set; }
        public CanadianAddressInfo CanadianAddressInfo { get; set; }
        public Error Error { get; set; }
        public override string ToString()
        {
            return $"AVCA2_Response: [CanadianAddressInfoV2={CanadianAddressInfoV2}, Error={Error}]";
        }
    }
    public class CanadianAddressInfoV2
    {
        public string Address { get; set; }
        public string Address2 { get; set; }
        public string Municipality { get; set; }
        public string Province { get; set; }
        public string PostalCode { get; set; }
        public string TimeZone { get; set; }
        public string AddressNumberFragment { get; set; }
        public string StreetNameFragment { get; set; }
        public string StreetTypeFragment { get; set; }
        public string DirectionalCodeFragment { get; set; }
        public string UnitTypeFragment { get; set; }
        public string UnitNumberFragment { get; set; }
        public string IsPOBox { get; set; }
        public string BoxNumberFragment { get; set; }
        public string StationInfo { get; set; }
        public string DeliveryMode { get; set; }
        public string DeliveryInstallation { get; set; }
        public string Corrections { get; set; }
        public string CorrectionsDescriptions { get; set; }
        public override string ToString()
        {
            StringBuilder sb = new StringBuilder();
            sb.AppendLine($"Address: {Address}");
            sb.AppendLine($"Address2: {Address2}");
            sb.AppendLine($"Municipality: {Municipality}");
            sb.AppendLine($"Province: {Province}");
            sb.AppendLine($"PostalCode: {PostalCode}");
            sb.AppendLine($"TimeZone: {TimeZone}");
            sb.AppendLine($"AddressNumberFragment: {AddressNumberFragment}");
            sb.AppendLine($"StreetNameFragment: {StreetNameFragment}");
            sb.AppendLine($"StreetTypeFragment: {StreetTypeFragment}");
            sb.AppendLine($"DirectionalCodeFragment: {DirectionalCodeFragment}");
            sb.AppendLine($"UnitTypeFragment: {UnitTypeFragment}");
            sb.AppendLine($"UnitNumberFragment: {UnitNumberFragment}");
            sb.AppendLine($"IsPOBox: {IsPOBox}");
            sb.AppendLine($"BoxNumberFragment: {BoxNumberFragment}");
            sb.AppendLine($"StationInfo: {StationInfo}");
            sb.AppendLine($"DeliveryMode: {DeliveryMode}");
            sb.AppendLine($"DeliveryInstallation: {DeliveryInstallation}");
            sb.AppendLine($"Corrections: {Corrections}");
            sb.AppendLine($"CorrectionsDescriptions: {CorrectionsDescriptions}");

            return sb.ToString();
        }
    }
    public class Error
    {
        public string Type { get; set; }
        public string TypeCode { get; set; }
        public string Desc { get; set; }
        public string DescCode { get; set; }
        public override string ToString()
        {
            return $"Type: {Type} " +
                $"TypeCode: {TypeCode} " +
                $"Desc: {Desc} " +
                $"DescCode: {DescCode} ";
        }
    }
    public class CanadianAddressInfo
    {
        public string Address { get; set; }
        public string Address2 { get; set; }
        public string Municipality { get; set; }
        public string Province { get; set; }
        public string PostalCode { get; set; }
        public string TimeZone { get; set; }
        public string AddressNumberFragment { get; set; }
        public string StreetNameFragment { get; set; }
        public string StreetTypeFragment { get; set; }
        public string DirectionalCodeFragment { get; set; }
        public string UnitTypeFragment { get; set; }
        public string UnitNumberFragment { get; set; }
        public string IsPOBox { get; set; }
        public string BoxNumberFragment { get; set; }
        public string StationInfo { get; set; }
        public string DeliveryMode { get; set; }
        public string DeliveryInstallation { get; set; }

        public override string ToString()
        {
            var sb = new StringBuilder();
            sb.AppendLine($"Address: {Address}");
            sb.AppendLine($"Address2: {Address2}");
            sb.AppendLine($"Municipality: {Municipality}");
            sb.AppendLine($"Province: {Province}");
            sb.AppendLine($"PostalCode: {PostalCode}");
            sb.AppendLine($"TimeZone: {TimeZone}");
            sb.AppendLine($"AddressNumberFragment: {AddressNumberFragment}");
            sb.AppendLine($"StreetNameFragment: {StreetNameFragment}");
            sb.AppendLine($"StreetTypeFragment: {StreetTypeFragment}");
            sb.AppendLine($"DirectionalCodeFragment: {DirectionalCodeFragment}");
            sb.AppendLine($"UnitTypeFragment: {UnitTypeFragment}");
            sb.AppendLine($"UnitNumberFragment: {UnitNumberFragment}");
            sb.AppendLine($"IsPOBox: {IsPOBox}");
            sb.AppendLine($"BoxNumberFragment: {BoxNumberFragment}");
            sb.AppendLine($"StationInfo: {StationInfo}");
            sb.AppendLine($"DeliveryMode: {DeliveryMode}");
            sb.AppendLine($"DeliveryInstallation: {DeliveryInstallation}");
            return sb.ToString();
        }
    }


}
