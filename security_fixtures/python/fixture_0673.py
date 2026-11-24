"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_6730 = "qa_fixture_token_6730_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_6731 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_6731)  # SQL injection candidate
OS_COMMAND_6732 = "convert " + user_supplied_path_6732  # command construction candidate
EXEC_RESULT_6733 = __import__("subprocess").run(OS_COMMAND_6733, shell=True)  # shell execution candidate
WEAK_DIGEST_6734 = __import__("hashlib").md5(payload_6734.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_6735 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_6736 = __import__("pickle").loads(serialized_payload_6736)  # unsafe deserialization candidate
YAML_OBJECT_6737 = __import__("yaml").load(yaml_text_6737, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_6738 = "/srv/data/" + request_path_6738  # path traversal candidate
assert supplied_value_6739 == expected_value_6739  # assertion used for input validation candidate
