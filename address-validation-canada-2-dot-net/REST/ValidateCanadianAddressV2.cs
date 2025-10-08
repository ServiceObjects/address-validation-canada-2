namespace address_validation_canada_2_dot_net.REST
{
    /// <summary>
    /// Provides functionality to call the ServiceObjects AVCA2 REST API's ValidateCanadianAddressV2 endpoint,
    /// retrieving validated Canadian address information (e.g., corrected address, municipality, province, postal code)
    /// for a given input with fallback to a backup endpoint for reliability in live mode.
    /// </summary>
    public static class ValidateCanadianAddressV2Client
    {
        // Base URL constants: production, backup, and trial
        private const string LiveBaseUrl = "https://sws.serviceobjects.com/AVCA2/api.svc/";
        private const string BackupBaseUrl = "https://swsbackup.serviceobjects.com/AVCA2/api.svc/";
        private const string TrialBaseUrl = "https://trial.serviceobjects.com/AVCA2/api.svc/";

        /// <summary>
        /// Synchronously calls the ValidateCanadianAddressV2 REST endpoint to retrieve validated address information,
        /// attempting the primary endpoint first and falling back to the backup if the response is invalid
        /// (Error.TypeCode == "3") in live mode.
        /// </summary>
        /// <param name="input">The input parameters including address, municipality, province, postal code, language, and license key.</param>
        /// <returns>Deserialized <see cref="AVCA2Response"/> containing validated address data or an error.</returns>
        public static AVCA2Response Invoke(ValidateCanadianAddressV2Input input)
        {
            // Use query string parameters so missing/optional fields don't break the URL
            string url = BuildUrl(input, input.IsLive ? LiveBaseUrl : TrialBaseUrl);
            AVCA2Response response = Helper.HttpGet<AVCA2Response>(url, input.TimeoutSeconds);

            // Fallback on error in live mode
            if (input.IsLive && !ValidResponse(response))
            {
                string fallbackUrl = BuildUrl(input, BackupBaseUrl);
                AVCA2Response fallbackResponse = Helper.HttpGet<AVCA2Response>(fallbackUrl, input.TimeoutSeconds);
                return fallbackResponse;
            }

            return response;
        }

        /// <summary>
        /// Asynchronously calls the ValidateCanadianAddressV2 REST endpoint to retrieve validated address information,
        /// attempting the primary endpoint first and falling back to the backup if the response is invalid
        /// (Error.TypeCode == "3") in live mode.
        /// </summary>
        /// <param name="input">The input parameters including address, municipality, province, postal code, language, and license key.</param>
        /// <returns>Deserialized <see cref="AVCA2Response"/> containing validated address data or an error.</returns>
        public static async Task<AVCA2Response> InvokeAsync(ValidateCanadianAddressV2Input input)
        {
            // Use query string parameters so missing/optional fields don't break the URL
            string url = BuildUrl(input, input.IsLive ? LiveBaseUrl : TrialBaseUrl);
            AVCA2Response response = await Helper.HttpGetAsync<AVCA2Response>(url, input.TimeoutSeconds).ConfigureAwait(false);

            // Fallback on error in live mode
            if (input.IsLive && !ValidResponse(response))
            {
                string fallbackUrl = BuildUrl(input, BackupBaseUrl);
                AVCA2Response fallbackResponse = await Helper.HttpGetAsync<AVCA2Response>(fallbackUrl, input.TimeoutSeconds).ConfigureAwait(false);
                return fallbackResponse;
            }

            return response;
        }

        // Build the full request URL, including URL-encoded query string
        public static string BuildUrl(ValidateCanadianAddressV2Input input, string baseUrl)
        {
            // Construct query string with URL-encoded parameters
            string qs = $"ValidateCanadianAddressV2?" +
                        $"Address={Helper.UrlEncode(input.Address)}" +
                        $"&Address2={Helper.UrlEncode(input.Address2)}" +
                        $"&Municipality={Helper.UrlEncode(input.Municipality)}" +
                        $"&Province={Helper.UrlEncode(input.Province)}" +
                        $"&PostalCode={Helper.UrlEncode(input.PostalCode)}" +
                        $"&Language={Helper.UrlEncode(input.Language)}" +
                        $"&LicenseKey={Helper.UrlEncode(input.LicenseKey)}" +
                        $"&Format=JSON";
            return baseUrl + qs;
        }

        private static bool ValidResponse(AVCA2Response response) => response?.Error == null || response.Error.TypeCode != "3";

        /// <summary>
        /// Input parameters for the ValidateCanadianAddressV2 API call. Represents a Canadian address to validate.
        /// </summary>
        /// <param name="Address">Address line of the address to validate (e.g., "50 Coach Hill Dr").</param>
        /// <param name="Address2">Secondary address line. Optional.</param>
        /// <param name="Municipality">The municipality of the address (e.g., "Kitchener"). Optional if postal code is provided.</param>
        /// <param name="Province">The province of the address (e.g., "Ont"). Optional if postal code is provided.</param>
        /// <param name="PostalCode">The postal code of the address (e.g., "N2E 1P4"). Optional if municipality and province are provided.</param>
        /// <param name="Language">The language for the response (e.g., "EN", "FR", "EN-Proper"). Optional.</param>
        /// <param name="LicenseKey">The license key to authenticate the API request.</param>
        /// <param name="IsLive">Indicates whether to use the live service (true) or trial service (false).</param>
        /// <param name="TimeoutSeconds">Timeout duration for the API call, in seconds.</param>
        public record ValidateCanadianAddressV2Input(
            string Address = "",
            string Address2 = "",
            string Municipality = "",
            string Province = "",
            string PostalCode = "",
            string Language = "",
            string LicenseKey = "",
            bool IsLive = true,
            int TimeoutSeconds = 15
        );
    }
}