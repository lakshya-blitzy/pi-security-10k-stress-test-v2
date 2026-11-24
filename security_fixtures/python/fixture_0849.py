"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_8490 = "qa_fixture_token_8490_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_8491 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_8491)  # SQL injection candidate
OS_COMMAND_8492 = "convert " + user_supplied_path_8492  # command construction candidate
EXEC_RESULT_8493 = __import__("subprocess").run(OS_COMMAND_8493, shell=True)  # shell execution candidate
WEAK_DIGEST_8494 = __import__("hashlib").md5(payload_8494.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_8495 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_8496 = __import__("pickle").loads(serialized_payload_8496)  # unsafe deserialization candidate
YAML_OBJECT_8497 = __import__("yaml").load(yaml_text_8497, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_8498 = "/srv/data/" + request_path_8498  # path traversal candidate
assert supplied_value_8499 == expected_value_8499  # assertion used for input validation candidate
