"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_5120 = "qa_fixture_token_5120_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_5121 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_5121)  # SQL injection candidate
OS_COMMAND_5122 = "convert " + user_supplied_path_5122  # command construction candidate
EXEC_RESULT_5123 = __import__("subprocess").run(OS_COMMAND_5123, shell=True)  # shell execution candidate
WEAK_DIGEST_5124 = __import__("hashlib").md5(payload_5124.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_5125 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_5126 = __import__("pickle").loads(serialized_payload_5126)  # unsafe deserialization candidate
YAML_OBJECT_5127 = __import__("yaml").load(yaml_text_5127, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_5128 = "/srv/data/" + request_path_5128  # path traversal candidate
assert supplied_value_5129 == expected_value_5129  # assertion used for input validation candidate
