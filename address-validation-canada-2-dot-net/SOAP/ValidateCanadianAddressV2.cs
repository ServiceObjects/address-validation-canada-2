using AVCA2Reference;

namespace address_validation_canada_2_dot_net.SOAP
{
    /// <summary>
    /// Provides functionality to call the ServiceObjects AVCA2 SOAP service's ValidateCanadianAddressV2 operation,
    /// retrieving validated Canadian address information (e.g., corrected address, municipality, province, postal code)
    /// for a given input with fallback to a backup endpoint for reliability in live mode.
    /// </summary>
    public class ValidateCanadianAddressV2Validation
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
        public ValidateCanadianAddressV2Validation(bool isLive)
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
        /// This operation returns validated Canadian address information, including corrected address,
        /// municipality, province, postal code, and additional details like time zone and PO Box status.
        /// </summary>
        /// <param name="Address">Address line of the address to validate (e.g., "50 Coach Hill Dr").</param>
        /// <param name="Address2">Secondary address line (e.g., "Apt 4B"). Optional.</param>
        /// <param name="Municipality">The municipality of the address (e.g., "Kitchener"). Optional if postal code is provided.</param>
        /// <param name="Province">The province of the address (e.g., "Ont"). Optional if postal code is provided.</param>
        /// <param name="PostalCode">The postal code of the address (e.g., "N2E 1P4"). Optional if municipality and province are provided.</param>
        /// <param name="Language">The language for the response (e.g., "EN", "FR", "EN-Proper"). Optional.</param>
        /// <param name="LicenseKey">The license key to authenticate the API request.</param>
        public async Task<CanadianAddressResponseV2> ValidateCanadianAddressV2(string Address, string Address2, string Municipality, string Province, string PostalCode, string Language, string LicenseKey)
        {
            ValidateCanada2Client clientPrimary = null;
            ValidateCanada2Client clientBackup = null;

            try
            {
                // Attempt Primary
                clientPrimary = new ValidateCanada2Client();
                clientPrimary.Endpoint.Address = new System.ServiceModel.EndpointAddress(_primaryUrl);
                clientPrimary.InnerChannel.OperationTimeout = TimeSpan.FromMilliseconds(_timeoutMs);

                CanadianAddressResponseV2 response = await clientPrimary.ValidateCanadianAddressV2Async(
                    Address, Address2, Municipality, Province, PostalCode, Language, LicenseKey).ConfigureAwait(false);

                if (_isLive && !ValidResponse(response))
                {
                    throw new InvalidOperationException("Primary endpoint returned null or a fatal error (TypeCode=3) for ValidateCanadianAddressV2");
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

                    return await clientBackup.ValidateCanadianAddressV2Async(
                        Address, Address2, Municipality, Province, PostalCode, Language, LicenseKey).ConfigureAwait(false);
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
        private static bool ValidResponse(CanadianAddressResponseV2 response) => response?.Error == null || response.Error.TypeCode != "3";
    }
}