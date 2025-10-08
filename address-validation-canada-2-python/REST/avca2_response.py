from dataclasses import dataclass
from typing import Optional, List

@dataclass
class Error:
    Type: Optional[str] = None
    TypeCode: Optional[str] = None
    Desc: Optional[str] = None
    DescCode: Optional[str] = None

    def __str__(self) -> str:
        return (f"Error: Type={self.Type}, TypeCode={self.TypeCode}, Desc={self.Desc}, "
                f"DescCode={self.DescCode}")

@dataclass
class CanadianAddressInfo:
    Address: Optional[str] = None
    Address2: Optional[str] = None
    Municipality: Optional[str] = None
    Province: Optional[str] = None
    PostalCode: Optional[str] = None
    TimeZone: Optional[str] = None
    AddressNumberFragment: Optional[str] = None
    StreetNameFragment: Optional[str] = None
    StreetTypeFragment: Optional[str] = None
    DirectionalCodeFragment: Optional[str] = None
    UnitTypeFragment: Optional[str] = None
    UnitNumberFragment: Optional[str] = None
    IsPOBox: Optional[bool] = None
    BoxNumberFragment: Optional[str] = None
    StationInfo: Optional[str] = None
    DeliveryMode: Optional[str] = None
    DeliveryInstallation: Optional[str] = None

    def __str__(self) -> str:
        return (f"CanadianAddressInfo: Address={self.Address}, Address2={self.Address2}, "
                f"Municipality={self.Municipality}, Province={self.Province}, PostalCode={self.PostalCode}, "
                f"TimeZone={self.TimeZone}, AddressNumberFragment={self.AddressNumberFragment}, "
                f"StreetNameFragment={self.StreetNameFragment}, StreetTypeFragment={self.StreetTypeFragment}, "
                f"DirectionalCodeFragment={self.DirectionalCodeFragment}, UnitTypeFragment={self.UnitTypeFragment}, "
                f"UnitNumberFragment={self.UnitNumberFragment}, IsPOBox={self.IsPOBox}, "
                f"BoxNumberFragment={self.BoxNumberFragment}, StationInfo={self.StationInfo}, "
                f"DeliveryMode={self.DeliveryMode}, DeliveryInstallation={self.DeliveryInstallation}")

@dataclass
class CanadianAddressInfoV2:
    Address: Optional[str] = None
    Address2: Optional[str] = None
    Municipality: Optional[str] = None
    Province: Optional[str] = None
    PostalCode: Optional[str] = None
    TimeZone: Optional[str] = None
    AddressNumberFragment: Optional[str] = None
    StreetNameFragment: Optional[str] = None
    StreetTypeFragment: Optional[str] = None
    DirectionalCodeFragment: Optional[str] = None
    UnitTypeFragment: Optional[str] = None
    UnitNumberFragment: Optional[str] = None
    IsPOBox: Optional[bool] = None
    BoxNumberFragment: Optional[str] = None
    StationInfo: Optional[str] = None
    DeliveryMode: Optional[str] = None
    DeliveryInstallation: Optional[str] = None
    Corrections: Optional[str] = None
    CorrectionsDescriptions: Optional[str] = None

    def __str__(self) -> str:
        return (f"CanadianAddressInfoV2: Address={self.Address}, Address2={self.Address2}, "
                f"Municipality={self.Municipality}, Province={self.Province}, PostalCode={self.PostalCode}, "
                f"TimeZone={self.TimeZone}, AddressNumberFragment={self.AddressNumberFragment}, "
                f"StreetNameFragment={self.StreetNameFragment}, StreetTypeFragment={self.StreetTypeFragment}, "
                f"DirectionalCodeFragment={self.DirectionalCodeFragment}, UnitTypeFragment={self.UnitTypeFragment}, "
                f"UnitNumberFragment={self.UnitNumberFragment}, IsPOBox={self.IsPOBox}, "
                f"BoxNumberFragment={self.BoxNumberFragment}, StationInfo={self.StationInfo}, "
                f"DeliveryMode={self.DeliveryMode}, DeliveryInstallation={self.DeliveryInstallation}, "
                f"Corrections={self.Corrections}, CorrectionsDescriptions={self.CorrectionsDescriptions}")

@dataclass
class AVCA2Response:
    CanadianAddressInfoV2: Optional['CanadianAddressInfoV2'] = None
    CanadianAddressInfo: Optional['CanadianAddressInfo'] = None
    Error: Optional['Error'] = None

    def __str__(self) -> str:
        address_info_v2 = str(self.CanadianAddressInfoV2) if self.CanadianAddressInfoV2 else 'None'
        address_info = str(self.CanadianAddressInfo) if self.CanadianAddressInfo else 'None'
        error = str(self.Error) if self.Error else 'None'
        return (f"AVCA2Response: CanadianAddressInfoV2={address_info_v2}, "
                f"CanadianAddressInfo={address_info}, Error={error}]")