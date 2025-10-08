from avca2_response import AVCA2Response, CanadianAddressInfo, Error
import requests

# Endpoint URLs for ServiceObjects AVCA2 (Address Validation - Canada) API
primary_url = "https://sws.serviceobjects.com/AVCA2/api.svc/ValidateCanadianMunicipalityProvince?"
backup_url = "https://swsbackup.serviceobjects.com/AVCA2/api.svc/ValidateCanadianMunicipalityProvince?"
trial_url = "https://trial.serviceobjects.com/AVCA2/api.svc/ValidateCanadianMunicipalityProvince?"

def validate_canadian_municipality_province(
    municipality: str,
    province: str,
    postal_code: str,
    license_key: str,
    is_live: bool = True,
    timeout_seconds: int = 15
) -> AVCA2Response:
    """
    Call ServiceObjects AVCA2 API's ValidateCanadianMunicipalityProvince endpoint
    to retrieve validated Canadian municipality and province information for a given address.

    Parameters:
        municipality: The municipality of the address (e.g., "Bowen Island"). Optional if postal code is provided.
        province: The province of the address (e.g., "BC"). Optional if postal code is provided.
        postal_code: The postal code of the address (e.g., "V0N 1G2"). Optional if municipality and province are provided.
        license_key: Your ServiceObjects license key.
        is_live: Use live or trial servers.
        timeout_seconds: Timeout for the HTTP request in seconds.

    Returns:
        AVCA2Response: Parsed JSON response with validated address details or error details.

    Raises:
        RuntimeError: If the API returns an error payload.
        requests.RequestException: On network/HTTP failures (trial mode).
    """
    params = {
        "Municipality": municipality,
        "Province": province,
        "PostalCode": postal_code,
        "LicenseKey": license_key,
        "Format":"JSON"
    }
    # Select the base URL: production vs trial
    url = primary_url if is_live else trial_url

    try:
        # Attempt primary (or trial) endpoint
        response = requests.get(url, params=params, timeout=timeout_seconds)
        response.raise_for_status()
        data = response.json()

        # If API returned an error in JSON payload, trigger fallback
        error = data.get('Error')
        if not (error is None or error.get('TypeCode') != "3"):
            if is_live:
                # Try backup URL
                response = requests.get(backup_url, params=params, timeout=timeout_seconds)
                response.raise_for_status()
                data = response.json()

                # If still error, propagate exception
                if 'Error' in data:
                    raise RuntimeError(f"AVCA2 service error: {data['Error']}")
            else:
                # Trial mode error is terminal
                raise RuntimeError(f"AVCA2 trial error: {data['Error']}")

        # Convert JSON response to AVCA2Response for structured access
        error = Error(**data.get("Error", {})) if data.get("Error") else None

        return AVCA2Response(
            CanadianAddressInfo=CanadianAddressInfo(
                Address=data.get("CanadianAddressInfo", {}).get("Address"),
                Address2=data.get("CanadianAddressInfo", {}).get("Address2"),
                Municipality=data.get("CanadianAddressInfo", {}).get("Municipality"),
                Province=data.get("CanadianAddressInfo", {}).get("Province"),
                PostalCode=data.get("CanadianAddressInfo", {}).get("PostalCode"),
                TimeZone=data.get("CanadianAddressInfo", {}).get("TimeZone"),
                AddressNumberFragment=data.get("CanadianAddressInfo", {}).get("AddressNumberFragment"),
                StreetNameFragment=data.get("CanadianAddressInfo", {}).get("StreetNameFragment"),
                StreetTypeFragment=data.get("CanadianAddressInfo", {}).get("StreetTypeFragment"),
                DirectionalCodeFragment=data.get("CanadianAddressInfo", {}).get("DirectionalCodeFragment"),
                UnitTypeFragment=data.get("CanadianAddressInfo", {}).get("UnitTypeFragment"),
                UnitNumberFragment=data.get("CanadianAddressInfo", {}).get("UnitNumberFragment"),
                IsPOBox=data.get("CanadianAddressInfo", {}).get("IsPOBox"),
                BoxNumberFragment=data.get("CanadianAddressInfo", {}).get("BoxNumberFragment"),
                StationInfo=data.get("CanadianAddressInfo", {}).get("StationInfo"),
                DeliveryMode=data.get("CanadianAddressInfo", {}).get("DeliveryMode"),
                DeliveryInstallation=data.get("CanadianAddressInfo", {}).get("DeliveryInstallation")
            ) if data.get("CanadianAddressInfo") else None,
            Error=error,
        )

    except requests.RequestException as req_exc:
        # Network or HTTP-level error occurred
        if is_live:
            try:
                # Fallback to backup URL
                response = requests.get(backup_url, params=params, timeout=timeout_seconds)
                response.raise_for_status()
                data = response.json()
                if "Error" in data:
                    raise RuntimeError(f"AVCA2 backup error: {data['Error']}") from req_exc

                error = Error(**data.get("Error", {})) if data.get("Error") else None

                return AVCA2Response(
                    CanadianAddressInfo=CanadianAddressInfo(
                        Address=data.get("CanadianAddressInfo", {}).get("Address"),
                        Address2=data.get("CanadianAddressInfo", {}).get("Address2"),
                        Municipality=data.get("CanadianAddressInfo", {}).get("Municipality"),
                        Province=data.get("CanadianAddressInfo", {}).get("Province"),
                        PostalCode=data.get("CanadianAddressInfo", {}).get("PostalCode"),
                        TimeZone=data.get("CanadianAddressInfo", {}).get("TimeZone"),
                        AddressNumberFragment=data.get("CanadianAddressInfo", {}).get("AddressNumberFragment"),
                        StreetNameFragment=data.get("CanadianAddressInfo", {}).get("StreetNameFragment"),
                        StreetTypeFragment=data.get("CanadianAddressInfo", {}).get("StreetTypeFragment"),
                        DirectionalCodeFragment=data.get("CanadianAddressInfo", {}).get("DirectionalCodeFragment"),
                        UnitTypeFragment=data.get("CanadianAddressInfo", {}).get("UnitTypeFragment"),
                        UnitNumberFragment=data.get("CanadianAddressInfo", {}).get("UnitNumberFragment"),
                        IsPOBox=data.get("CanadianAddressInfo", {}).get("IsPOBox"),
                        BoxNumberFragment=data.get("CanadianAddressInfo", {}).get("BoxNumberFragment"),
                        StationInfo=data.get("CanadianAddressInfo", {}).get("StationInfo"),
                        DeliveryMode=data.get("CanadianAddressInfo", {}).get("DeliveryMode"),
                        DeliveryInstallation=data.get("CanadianAddressInfo", {}).get("DeliveryInstallation")
                    ) if data.get("CanadianAddressInfo") else None,
                    Error=error,
                )
            except Exception as backup_exc:
                raise RuntimeError("AVCA2 service unreachable on both endpoints") from backup_exc
        else:
            raise RuntimeError(f"AVCA2 trial error: {str(req_exc)}") from req_exc