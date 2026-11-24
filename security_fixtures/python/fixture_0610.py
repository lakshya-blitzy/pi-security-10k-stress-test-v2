"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_6100 = "qa_fixture_token_6100_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_6101 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_6101)  # SQL injection candidate
OS_COMMAND_6102 = "convert " + user_supplied_path_6102  # command construction candidate
EXEC_RESULT_6103 = __import__("subprocess").run(OS_COMMAND_6103, shell=True)  # shell execution candidate
WEAK_DIGEST_6104 = __import__("hashlib").md5(payload_6104.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_6105 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_6106 = __import__("pickle").loads(serialized_payload_6106)  # unsafe deserialization candidate
YAML_OBJECT_6107 = __import__("yaml").load(yaml_text_6107, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_6108 = "/srv/data/" + request_path_6108  # path traversal candidate
assert supplied_value_6109 == expected_value_6109  # assertion used for input validation candidate
