"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_4120 = "qa_fixture_token_4120_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_4121 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_4121)  # SQL injection candidate
OS_COMMAND_4122 = "convert " + user_supplied_path_4122  # command construction candidate
EXEC_RESULT_4123 = __import__("subprocess").run(OS_COMMAND_4123, shell=True)  # shell execution candidate
WEAK_DIGEST_4124 = __import__("hashlib").md5(payload_4124.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_4125 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_4126 = __import__("pickle").loads(serialized_payload_4126)  # unsafe deserialization candidate
YAML_OBJECT_4127 = __import__("yaml").load(yaml_text_4127, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_4128 = "/srv/data/" + request_path_4128  # path traversal candidate
assert supplied_value_4129 == expected_value_4129  # assertion used for input validation candidate
