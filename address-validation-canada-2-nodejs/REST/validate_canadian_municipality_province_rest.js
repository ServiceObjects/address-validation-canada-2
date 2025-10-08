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
 * Constructs a full URL for the ValidateCanadianMunicipalityProvince API endpoint by combining the base URL
 * with query parameters derived from the input parameters.
 * @param {Object} params - An object containing all the input parameters.
 * @param {string} baseUrl - The base URL for the API service (live, backup, or trial).
 * @returns {string} The constructed URL with query parameters.
 */
const buildUrl = (params, baseUrl) =>
    `${baseUrl}ValidateCanadianMunicipalityProvince?${querystring.stringify(params)}`;

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
 * Provides functionality to call the ServiceObjects AVCA2 API's ValidateCanadianMunicipalityProvince endpoint,
 * retrieving validated Canadian municipality and province information with fallback to a backup endpoint for reliability in live mode.
 */
const ValidateCanadianMunicipalityProvinceClient = {
    /**
     * @summary
     * Asynchronously invokes the ValidateCanadianMunicipalityProvince API endpoint, attempting the primary endpoint
     * first and falling back to the backup if the response is invalid (Error.TypeCode == '3') in live mode.
     * @param {string} Municipality - The municipality of the address (e.g., "Toronto"). Optional if postal code is provided.
     * @param {string} Province - The province of the address (e.g., "ON"). Optional if postal code is provided.
     * @param {string} PostalCode - The postal code of the address (e.g., "M5V 2T6"). Optional if municipality and province are provided.
     * @param {string} LicenseKey - Your license key to use the service.
     * @param {boolean} isLive - Value to determine whether to use the live or trial servers.
     * @param {number} timeoutSeconds - Timeout, in seconds, for the call to the service.
     * @returns {Promise<AVCA2Response>} A promise that resolves to an AVCA2Response object.
     */
    async invokeAsync(Municipality, Province, PostalCode, LicenseKey, isLive = true, timeoutSeconds = 15) {
        const params = {
            Municipality,
            Province,
            PostalCode,
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
     * Synchronously invokes the ValidateCanadianMunicipalityProvince API endpoint by wrapping the async call
     * and awaiting its result immediately.
     * @param {string} Municipality - The municipality of the address (e.g., "Bowen Island"). Optional if postal code is provided.
     * @param {string} Province - The province of the address (e.g., "BC"). Optional if postal code is provided.
     * @param {string} PostalCode - The postal code of the address (e.g., "V0N 1G2"). Optional if municipality and province are provided.
     * @param {string} LicenseKey - Your license key to use the service.
     * @param {boolean} isLive - Value to determine whether to use the live or trial servers.
     * @param {number} timeoutSeconds - Timeout, in seconds, for the call to the service.
     * @returns {AVCA2Response} An AVCA2Response object with validated municipality and province details or an error.
     */
    invoke(Municipality, Province, PostalCode, LicenseKey, isLive = true, timeoutSeconds = 15) {
        return (async () => await this.invokeAsync(
            Municipality, Province, PostalCode, LicenseKey, isLive, timeoutSeconds
        ))();
    }
};

export { ValidateCanadianMunicipalityProvinceClient, AVCA2Response };