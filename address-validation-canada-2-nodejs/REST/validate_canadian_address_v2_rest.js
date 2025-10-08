import axios from 'axios';
import querystring from 'querystring';
import { AVCA2Response } from './avca2_response.js';

/**
 * @constant
 * @type {string}
 * @description The base URL for the live ServiceObjects AVCA2 (Address Validation - Canada) API service.
 */
const LiveBaseUrl = 'https://sws.serviceobjects.com/AVCA2/api.svc/';

/**
 * @constant
 * @type {string}
 * @description The base URL for the backup ServiceObjects AVCA2 API service.
 */
const BackupBaseUrl = 'https://swsbackup.serviceobjects.com/AVCA2/api.svc/';

/**
 * @constant
 * @type {string}
 * @description The base URL for the trial ServiceObjects AVCA2 API service.
 */
const TrialBaseUrl = 'https://trial.serviceobjects.com/AVCA2/api.svc/';

/**
 * @summary
 * Checks if a response from the API is valid by verifying that it either has no Error object
 * or the Error.TypeCode is not equal to '3'.
 * @param {Object} response - The API response object to validate.
 * @returns {boolean} True if the response is valid, false otherwise.
 */
const isValid = (response) => !response?.Error || response.Error.TypeCode !== '3';

/**
 * @summary
 * Constructs a full URL for the ValidateCanadianAddressV2 API endpoint by combining the base URL
 * with query parameters derived from the input parameters.
 * @param {Object} params - An object containing all the input parameters.
 * @param {string} baseUrl - The base URL for the API service (live, backup, or trial).
 * @returns {string} The constructed URL with query parameters.
 */
const buildUrl = (params, baseUrl) =>
    `${baseUrl}ValidateCanadianAddressV2?${querystring.stringify(params)}`;

/**
 * @summary
 * Performs an HTTP GET request to the specified URL with a given timeout.
 * @param {string} url - The URL to send the GET request to.
 * @param {number} timeoutSeconds - The timeout duration in seconds for the request.
 * @returns {Promise<AVCA2Response>} A promise that resolves to an AVCA2Response object containing the API response data.
 * @throws {Error} Thrown if the HTTP request fails, with a message detailing the error.
 */
const httpGet = async (url, timeoutSeconds) => {
    try {
        const response = await axios.get(url, { timeout: timeoutSeconds * 1000 });
        return new AVCA2Response(response.data);
    } catch (error) {
        throw new Error(`HTTP request failed: ${error.message}`);
    }
};

/**
 * @summary
 * Provides functionality to call the ServiceObjects AVCA2 API's ValidateCanadianAddressV2 endpoint,
 * retrieving validated Canadian address information with fallback to a backup endpoint for reliability in live mode.
 */
const ValidateCanadianAddressV2Client = {
    /**
     * @summary
     * Asynchronously invokes the ValidateCanadianAddressV2 API endpoint, attempting the primary endpoint
     * first and falling back to the backup if the response is invalid (Error.TypeCode == '3') in live mode.
     * @param {string} Address - Address line of the address to validate (e.g., "50 Coach Hill Dr").
     * @param {string} Address2 - Secondary address line (e.g., "Apt 4B"). Optional.
     * @param {string} Municipality - The municipality of the address (e.g., "Kitchener"). Optional if postal code is provided.
     * @param {string} Province - The province of the address (e.g., "Ont"). Optional if postal code is provided.
     * @param {string} PostalCode - The postal code of the address (e.g., "N2E 1P4"). Optional if municipality and province are provided.
     * @param {string} Language - The language for the response (e.g., "EN", "FR", "EN-Proper", "FR-Proper"). Optional.
     * @param {string} LicenseKey - Your license key to use the service.
     * @param {boolean} isLive - Value to determine whether to use the live or trial servers.
     * @param {number} timeoutSeconds - Timeout, in seconds, for the call to the service.
     * @returns {Promise<AVCA2Response>} A promise that resolves to an AVCA2Response object.
     */
    async invokeAsync(Address, Address2, Municipality, Province, PostalCode, Language, LicenseKey, isLive = true, timeoutSeconds = 15) {
        const params = {
            Address,
            Address2,
            Municipality,
            Province,
            PostalCode,
            Language,
            LicenseKey,
            Format: 'JSON'
        };

        const url = buildUrl(params, isLive ? LiveBaseUrl : TrialBaseUrl);
        let response = await httpGet(url, timeoutSeconds);

        if (isLive && !isValid(response)) {
            const fallbackUrl = buildUrl(params, BackupBaseUrl);
            const fallbackResponse = await httpGet(fallbackUrl, timeoutSeconds);
            return fallbackResponse;
        }
        return response;
    },

    /**
     * @summary
     * Synchronously invokes the ValidateCanadianAddressV2 API endpoint by wrapping the async call
     * and awaiting its result immediately.
     * @param {string} Address - Address line of the address to validate (e.g., "50 Coach Hill Dr").
     * @param {string} Address2 - Secondary address line (e.g., "Apt 4B"). Optional.
     * @param {string} Municipality - The municipality of the address (e.g., "Kitchener"). Optional if postal code is provided.
     * @param {string} Province - The province of the address (e.g., "Ont"). Optional if postal code is provided.
     * @param {string} PostalCode - The postal code of the address (e.g., "N2E 1P4"). Optional if municipality and province are provided.
     * @param {string} Language - The language for the response (e.g., "EN", "FR", "EN-Proper", "FR-Proper"). Optional.
     * @param {string} LicenseKey - Your license key to use the service.
     * @param {boolean} isLive - Value to determine whether to use the live or trial servers.
     * @param {number} timeoutSeconds - Timeout, in seconds, for the call to the service.
     * @returns {AVCA2Response} An AVCA2Response object with validated address details or an error.
     */
    invoke(Address, Address2, Municipality, Province, PostalCode, Language, LicenseKey, isLive = true, timeoutSeconds = 15) {
        return (async () => await this.invokeAsync(
            Address, Address2, Municipality, Province, PostalCode, Language, LicenseKey, isLive, timeoutSeconds
        ))();
    }
};

export { ValidateCanadianAddressV2Client, AVCA2Response };