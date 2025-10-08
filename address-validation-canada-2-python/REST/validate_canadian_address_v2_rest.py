from avca2_response import AVCA2Response, CanadianAddressInfoV2, Error
import requests

# Endpoint URLs for ServiceObjects AVCA2 (Address Validation - Canada) API
primary_url = "https://sws.serviceobjects.com/AVCA2/api.svc/ValidateCanadianAddressV2?"
backup_url = "https://swsbackup.serviceobjects.com/AVCA2/api.svc/ValidateCanadianAddressV2?"
trial_url = "https://trial.serviceobjects.com/AVCA2/api.svc/ValidateCanadianAddressV2?"

def validate_canadian_address_v2(
    address: str,
    address2: str,
    municipality: str,
    province: str,
    postal_code: str,
    language: str,
    license_key: str,
    is_live: bool,
    timeout_seconds: int = 15
) -> AVCA2Response:
    """
    Call ServiceObjects AVCA2 API's ValidateCanadianAddressV2 endpoint
    to retrieve validated Canadian address information for a given address.

    Parameters:
        address: Address line of the address to validate (e.g., "50 Coach Hill Dr").
        address2: Secondary address line (e.g., "Apt 4B"). Optional.
        municipality: The municipality of the address (e.g., "Kitchener"). Optional if postal code is provided.
        province: The province of the address (e.g., "Ont"). Optional if postal code is provided.
        postal_code: The postal code of the address (e.g., "N2E 1P4"). Optional if municipality and province are provided.
        language: The language for the response (e.g., "EN", "FR", "EN-Proper", "FR-Proper"). Optional.
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
        "Address": address,
        "Address2": address2,
        "Municipality": municipality,
        "Province": province,
        "PostalCode": postal_code,
        "Language": language,
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
            CanadianAddressInfoV2=CanadianAddressInfoV2(
                Address=data.get("CanadianAddressInfoV2", {}).get("Address"),
                Address2=data.get("CanadianAddressInfoV2", {}).get("Address2"),
                Municipality=data.get("CanadianAddressInfoV2", {}).get("Municipality"),
                Province=data.get("CanadianAddressInfoV2", {}).get("Province"),
                PostalCode=data.get("CanadianAddressInfoV2", {}).get("PostalCode"),
                TimeZone=data.get("CanadianAddressInfoV2", {}).get("TimeZone"),
                AddressNumberFragment=data.get("CanadianAddressInfoV2", {}).get("AddressNumberFragment"),
                StreetNameFragment=data.get("CanadianAddressInfoV2", {}).get("StreetNameFragment"),
                StreetTypeFragment=data.get("CanadianAddressInfoV2", {}).get("StreetTypeFragment"),
                DirectionalCodeFragment=data.get("CanadianAddressInfoV2", {}).get("DirectionalCodeFragment"),
                UnitTypeFragment=data.get("CanadianAddressInfoV2", {}).get("UnitTypeFragment"),
                UnitNumberFragment=data.get("CanadianAddressInfoV2", {}).get("UnitNumberFragment"),
                IsPOBox=data.get("CanadianAddressInfoV2", {}).get("IsPOBox"),
                BoxNumberFragment=data.get("CanadianAddressInfoV2", {}).get("BoxNumberFragment"),
                StationInfo=data.get("CanadianAddressInfoV2", {}).get("StationInfo"),
                DeliveryMode=data.get("CanadianAddressInfoV2", {}).get("DeliveryMode"),
                DeliveryInstallation=data.get("CanadianAddressInfoV2", {}).get("DeliveryInstallation"),
                Corrections=data.get("CanadianAddressInfoV2", {}).get("Corrections"),
                CorrectionsDescriptions=data.get("CanadianAddressInfoV2", {}).get("CorrectionsDescriptions")
            ) if data.get("CanadianAddressInfoV2") else None,
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
                    CanadianAddressInfoV2=CanadianAddressInfoV2(
                        Address=data.get("CanadianAddressInfoV2", {}).get("Address"),
                        Address2=data.get("CanadianAddressInfoV2", {}).get("Address2"),
                        Municipality=data.get("CanadianAddressInfoV2", {}).get("Municipality"),
                        Province=data.get("CanadianAddressInfoV2", {}).get("Province"),
                        PostalCode=data.get("CanadianAddressInfoV2", {}).get("PostalCode"),
                        TimeZone=data.get("CanadianAddressInfoV2", {}).get("TimeZone"),
                        AddressNumberFragment=data.get("CanadianAddressInfoV2", {}).get("AddressNumberFragment"),
                        StreetNameFragment=data.get("CanadianAddressInfoV2", {}).get("StreetNameFragment"),
                        StreetTypeFragment=data.get("CanadianAddressInfoV2", {}).get("StreetTypeFragment"),
                        DirectionalCodeFragment=data.get("CanadianAddressInfoV2", {}).get("DirectionalCodeFragment"),
                        UnitTypeFragment=data.get("CanadianAddressInfoV2", {}).get("UnitTypeFragment"),
                        UnitNumberFragment=data.get("CanadianAddressInfoV2", {}).get("UnitNumberFragment"),
                        IsPOBox=data.get("CanadianAddressInfoV2", {}).get("IsPOBox"),
                        BoxNumberFragment=data.get("CanadianAddressInfoV2", {}).get("BoxNumberFragment"),
                        StationInfo=data.get("CanadianAddressInfoV2", {}).get("StationInfo"),
                        DeliveryMode=data.get("CanadianAddressInfoV2", {}).get("DeliveryMode"),
                        DeliveryInstallation=data.get("CanadianAddressInfoV2", {}).get("DeliveryInstallation"),
                        Corrections=data.get("CanadianAddressInfoV2", {}).get("Corrections"),
                        CorrectionsDescriptions=data.get("CanadianAddressInfoV2", {}).get("CorrectionsDescriptions")
                    ) if data.get("CanadianAddressInfoV2") else None,
                    Error=error,
                )
            except Exception as backup_exc:
                raise RuntimeError("AVCA2 service unreachable on both endpoints") from backup_exc
        else:
            raise RuntimeError(f"AVCA2 trial error: {str(req_exc)}") from req_exc