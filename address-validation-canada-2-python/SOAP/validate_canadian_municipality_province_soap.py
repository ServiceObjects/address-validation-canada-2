from suds.client import Client
from suds import WebFault
from suds.sudsobject import Object

class ValidateCanadianMunicipalityProvinceSoap:
    def __init__(self, license_key: str, is_live: bool = True, timeout_ms: int = 15000):
        """
        Initialize the ValidateCanadianMunicipalityProvinceSoap client for the ServiceObjects AVCA2 API.

        Parameters:
            license_key: Service Objects AVCA2 license key.
            is_live: Whether to use live or trial endpoints.
            timeout_ms: SOAP call timeout in milliseconds.
        """
        self.is_live = is_live
        self.timeout = timeout_ms / 1000.0
        self.license_key = license_key

        # WSDL URLs
        self._primary_wsdl = (
            "https://sws.serviceobjects.com/AVCA2/api.svc?wsdl"
            if is_live
            else "https://trial.serviceobjects.com/AVCA2/api.svc?wsdl"
        )
        self._backup_wsdl = (
            "https://swsbackup.serviceobjects.com/AVCA2/api.svc?wsdl"
            if is_live
            else "https://trial.serviceobjects.com/AVCA2/api.svc?wsdl"
        )

    def validate_canadian_municipality_province(
        self,
        municipality: str,
        province: str,
        postal_code: str
    ) -> Object:
        """
        Calls the ValidateCanadianMunicipalityProvince SOAP API to retrieve validated Canadian municipality and province information.

        Parameters:
            municipality: The municipality of the address (e.g., "Bowen Island"). Optional if postal code is provided.
            province: The province of the address (e.g., "BC"). Optional if postal code is provided.
            postal_code: The postal code of the address (e.g., "V0N 1G2"). Optional if municipality and province are provided.

        Returns:
            suds.sudsobject.Object: SOAP response containing validated address details or error.

        Raises:
            RuntimeError: If both primary and backup endpoints fail.
        """
        # Common kwargs for both calls
        call_kwargs = dict(
            Municipality=municipality,
            Province=province,
            PostalCode=postal_code,
            LicenseKey=self.license_key,
        )

        # Attempt primary
        try:
            client = Client(self._primary_wsdl)
            # Override endpoint URL if needed:
            response = client.service.ValidateCanadianMunicipalityProvince(**call_kwargs)

            # If response invalid or Error.TypeCode == "3", trigger fallback
            if response is None or (
                hasattr(response, "Error")
                and response.Error
                and response.Error.TypeCode == "3"
            ):
                raise ValueError("Primary returned no result or Error.TypeCode=3")

            return response

        except (WebFault, ValueError, Exception) as primary_ex:
            # Attempt backup
            try:
                client = Client(self._backup_wsdl)
                response = client.service.ValidateCanadianMunicipalityProvince(**call_kwargs)
                if response is None:
                    raise ValueError("Backup returned no result")
                return response
            except (WebFault, Exception) as backup_ex:
                msg = (
                    "Both primary and backup endpoints failed.\n"
                    f"Primary error: {str(primary_ex)}\n"
                    f"Backup error: {str(backup_ex)}"
                )
                raise RuntimeError(msg)