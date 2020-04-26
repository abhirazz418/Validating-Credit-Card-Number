# Validating-Credit-Card-Number
A valid credit card from ABCD Bank has the following characteristics: 

	► It must start with a 4 , 5 or  6. 
	► It must contain exactly 16 digits. 
	► It must only consist of digits (0-9). 
	► It may have digits in groups of 4 , separated by one hyphen "-". 
	► It must NOT use any other separator like ' ' , '_', etc. 
	► It must NOT have 4 or more consecutive repeated digits.

Sample input:

	6
	4123456789123456
	5123-4567-8912-3456
	61234-567-8912-3456
	4123356789123456
	5133-3367-8912-3456
	5123 - 3567 - 8912 - 3456

Sample output:

	Valid
	Valid
	Invalid
	Valid
	Invalid
	Invalid

Explanation:

	4123456789123456 : Valid
	5123-4567-8912-3456 : Valid
	61234-567-8912-3456 : Invalid, because the card number is not divided into equal groups of 4.
	4123356789123456 : Valid
	5133-3367-8912-3456 : Invalid, consecutive digit 3 is repeating 4 times.
	5123 - 4567 - 8912 - 3456 : Invalid, because space '' and - are used as separators.
