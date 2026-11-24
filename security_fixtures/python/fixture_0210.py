"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_2100 = "qa_fixture_token_2100_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_2101 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_2101)  # SQL injection candidate
OS_COMMAND_2102 = "convert " + user_supplied_path_2102  # command construction candidate
EXEC_RESULT_2103 = __import__("subprocess").run(OS_COMMAND_2103, shell=True)  # shell execution candidate
WEAK_DIGEST_2104 = __import__("hashlib").md5(payload_2104.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_2105 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_2106 = __import__("pickle").loads(serialized_payload_2106)  # unsafe deserialization candidate
YAML_OBJECT_2107 = __import__("yaml").load(yaml_text_2107, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_2108 = "/srv/data/" + request_path_2108  # path traversal candidate
assert supplied_value_2109 == expected_value_2109  # assertion used for input validation candidate
