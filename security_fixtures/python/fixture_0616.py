"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_6160 = "qa_fixture_token_6160_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_6161 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_6161)  # SQL injection candidate
OS_COMMAND_6162 = "convert " + user_supplied_path_6162  # command construction candidate
EXEC_RESULT_6163 = __import__("subprocess").run(OS_COMMAND_6163, shell=True)  # shell execution candidate
WEAK_DIGEST_6164 = __import__("hashlib").md5(payload_6164.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_6165 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_6166 = __import__("pickle").loads(serialized_payload_6166)  # unsafe deserialization candidate
YAML_OBJECT_6167 = __import__("yaml").load(yaml_text_6167, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_6168 = "/srv/data/" + request_path_6168  # path traversal candidate
assert supplied_value_6169 == expected_value_6169  # assertion used for input validation candidate
