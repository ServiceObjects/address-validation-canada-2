export class AVCA2Response {
    constructor(data = {}) {
        this.CanadianAddressInfoV2 = data.CanadianAddressInfoV2 ? new CanadianAddressInfoV2(data.CanadianAddressInfoV2) : null;
        this.CanadianAddressInfo = data.CanadianAddressInfo ? new CanadianAddressInfo(data.CanadianAddressInfo) : null;
        this.Error = data.Error ? new Error(data.Error) : null;
        this.Debug = data.Debug || [];
    }

    toString() {
        const debugString = this.Debug.length ? this.Debug.join(', ') : 'null';
        return `AVCA2Response: CanadianAddressInfoV2 = ${this.CanadianAddressInfoV2 ? this.CanadianAddressInfoV2.toString() : 'null'}, CanadianAddressInfo = ${this.CanadianAddressInfo ? this.CanadianAddressInfo.toString() : 'null'}, Error = ${this.Error ? this.Error.toString() : 'null'}, Debug = [${debugString}]`;
    }
}

export class CanadianAddressInfoV2 {
    constructor(data = {}) {
        this.Address = data.Address;
        this.Address2 = data.Address2;
        this.Municipality = data.Municipality;
        this.Province = data.Province;
        this.PostalCode = data.PostalCode;
        this.TimeZone = data.TimeZone;
        this.AddressNumberFragment = data.AddressNumberFragment;
        this.StreetNameFragment = data.StreetNameFragment;
        this.StreetTypeFragment = data.StreetTypeFragment;
        this.DirectionalCodeFragment = data.DirectionalCodeFragment;
        this.UnitTypeFragment = data.UnitTypeFragment;
        this.UnitNumberFragment = data.UnitNumberFragment;
        this.IsPOBox = data.IsPOBox;
        this.BoxNumberFragment = data.BoxNumberFragment;
        this.StationInfo = data.StationInfo;
        this.DeliveryMode = data.DeliveryMode;
        this.DeliveryInstallation = data.DeliveryInstallation;
        this.Corrections = data.Corrections;
        this.CorrectionsDescriptions = data.CorrectionsDescriptions;
    }

    toString() {
        return `CanadianAddressInfoV2: Address = ${this.Address}, Address2 = ${this.Address2}, Municipality = ${this.Municipality}, Province = ${this.Province}, PostalCode = ${this.PostalCode}, TimeZone = ${this.TimeZone}, AddressNumberFragment = ${this.AddressNumberFragment}, StreetNameFragment = ${this.StreetNameFragment}, StreetTypeFragment = ${this.StreetTypeFragment}, DirectionalCodeFragment = ${this.DirectionalCodeFragment}, UnitTypeFragment = ${this.UnitTypeFragment}, UnitNumberFragment = ${this.UnitNumberFragment}, IsPOBox = ${this.IsPOBox}, BoxNumberFragment = ${this.BoxNumberFragment}, StationInfo = ${this.StationInfo}, DeliveryMode = ${this.DeliveryMode}, DeliveryInstallation = ${this.DeliveryInstallation}, Corrections = ${this.Corrections}, CorrectionsDescriptions = ${this.CorrectionsDescriptions}`;
    }
}

export class Error {
    constructor(data = {}) {
        this.Type = data.Type;
        this.TypeCode = data.TypeCode;
        this.Desc = data.Desc;
        this.DescCode = data.DescCode;
    }

    toString() {
        return `Error: Type = ${this.Type}, TypeCode = ${this.TypeCode}, Desc = ${this.Desc}, DescCode = ${this.DescCode}`;
    }
}
export class CanadianAddressInfo {
    constructor(data = {}) {
        this.Address = data.Address;
        this.Address2 = data.Address2;
        this.Municipality = data.Municipality;
        this.Province = data.Province;
        this.PostalCode = data.PostalCode;
        this.TimeZone = data.TimeZone;
        this.AddressNumberFragment = data.AddressNumberFragment;
        this.StreetNameFragment = data.StreetNameFragment;
        this.StreetTypeFragment = data.StreetTypeFragment;
        this.DirectionalCodeFragment = data.DirectionalCodeFragment;
        this.UnitTypeFragment = data.UnitTypeFragment;
        this.UnitNumberFragment = data.UnitNumberFragment;
        this.IsPOBox = data.IsPOBox;
        this.BoxNumberFragment = data.BoxNumberFragment;
        this.StationInfo = data.StationInfo;
        this.DeliveryMode = data.DeliveryMode;
        this.DeliveryInstallation = data.DeliveryInstallation;
    }

    toString() {
        return `CanadianAddressInfo: Address = ${this.Address}, Address2 = ${this.Address2}, Municipality = ${this.Municipality}, Province = ${this.Province}, PostalCode = ${this.PostalCode}, TimeZone = ${this.TimeZone}, AddressNumberFragment = ${this.AddressNumberFragment}, StreetNameFragment = ${this.StreetNameFragment}, StreetTypeFragment = ${this.StreetTypeFragment}, DirectionalCodeFragment = ${this.DirectionalCodeFragment}, UnitTypeFragment = ${this.UnitTypeFragment}, UnitNumberFragment = ${this.UnitNumberFragment}, IsPOBox = ${this.IsPOBox}, BoxNumberFragment = ${this.BoxNumberFragment}, StationInfo = ${this.StationInfo}, DeliveryMode = ${this.DeliveryMode}, DeliveryInstallation = ${this.DeliveryInstallation}`;
    }
}

export default AVCA2Response;