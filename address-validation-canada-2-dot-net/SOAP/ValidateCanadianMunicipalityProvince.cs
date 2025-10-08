using AVCA2Reference;

namespace address_validation_canada_2_dot_net.SOAP
{
    /// <summary>
    /// Provides functionality to call the ServiceObjects AVCA2 SOAP service's ValidateCanadianMunicipalityProvince operation,
    /// retrieving validated Canadian municipality, province, and postal code information
    /// for a given input with fallback to a backup endpoint for reliability in live mode.
    /// </summary>
    public class ValidateCanadianMunicipalityProvinceValidation
    {
        private const string LiveBaseUrl = "https://sws.serviceobjects.com/AVCA2/api.svc/soap";
        private const string BackupBaseUrl = "https://swsbackup.serviceobjects.com/AVCA2/api.svc/soap";
        private const string TrialBaseUrl = "https://trial.serviceobjects.com/AVCA2/api.svc/soap";

        private readonly string _primaryUrl;
        private readonly string _backupUrl;
        private readonly int _timeoutMs;
        private readonly bool _isLive;

        /// <summary>
        /// Initializes URLs, timeout, and IsLive.
        /// </summary>
        public ValidateCanadianMunicipalityProvinceValidation(bool isLive)
        {
            _timeoutMs = 10000;
            _isLive = isLive;

            _primaryUrl = isLive ? LiveBaseUrl : TrialBaseUrl;
            _backupUrl = isLive ? BackupBaseUrl : TrialBaseUrl;

            if (string.IsNullOrWhiteSpace(_primaryUrl))
                throw new InvalidOperationException("Primary URL not set.");
            if (string.IsNullOrWhiteSpace(_backupUrl))
                throw new InvalidOperationException("Backup URL not set.");
        }

        /// <summary>
        /// This operation returns validated Canadian municipality, province, and postal code information,
        /// including additional details like time zone and delivery mode.
        /// </summary>
        /// <param name="Municipality">The municipality of the address (e.g., "Bowen Island"). Optional if postal code is provided.</param>
        /// <param name="Province">The province of the address (e.g., "BC"). Optional if postal code is provided.</param>
        /// <param name="PostalCode">The postal code of the address (e.g., "V0N 1G2"). Optional if municipality and province are provided.</param>
        /// <param name="LicenseKey">The license key to authenticate the API request.</param>
        public async Task<CanadianAddressResponse> ValidateCanadianMunicipalityProvince(string Municipality, string Province, string PostalCode, string LicenseKey)
        {
            ValidateCanada2Client clientPrimary = null;
            ValidateCanada2Client clientBackup = null;

            try
            {
                // Attempt Primary
                clientPrimary = new ValidateCanada2Client();
                clientPrimary.Endpoint.Address = new System.ServiceModel.EndpointAddress(_primaryUrl);
                clientPrimary.InnerChannel.OperationTimeout = TimeSpan.FromMilliseconds(_timeoutMs);

                CanadianAddressResponse response = await clientPrimary.ValidateCanadianMunicipalityProvinceAsync(
                    Municipality, Province, PostalCode, LicenseKey).ConfigureAwait(false);

                if (_isLive && !ValidResponse(response))
                {
                    throw new InvalidOperationException("Primary endpoint returned null or a fatal error (TypeCode=3) for ValidateCanadianMunicipalityProvince");
                }
                return response;
            }
            catch (Exception primaryEx)
            {
                try
                {
                    clientBackup = new ValidateCanada2Client();
                    clientBackup.Endpoint.Address = new System.ServiceModel.EndpointAddress(_backupUrl);
                    clientBackup.InnerChannel.OperationTimeout = TimeSpan.FromMilliseconds(_timeoutMs);

                    return await clientBackup.ValidateCanadianMunicipalityProvinceAsync(
                        Municipality, Province, PostalCode, LicenseKey).ConfigureAwait(false);
                }
                catch (Exception backupEx)
                {
                    throw new InvalidOperationException(
                        $"Both primary and backup endpoints failed.\n" +
                        $"Primary error: {primaryEx.Message}\n" +
                        $"Backup error: {backupEx.Message}");
                }
                finally
                {
                    clientBackup?.Close();
                }
            }
            finally
            {
                clientPrimary?.Close();
            }
        }

        private static bool ValidResponse(CanadianAddressResponse response) => response?.Error == null || response.Error.TypeCode != "3";
    }
}