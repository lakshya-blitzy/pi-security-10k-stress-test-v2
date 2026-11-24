"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_4160 = "qa_fixture_token_4160_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_4161 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_4161)  # SQL injection candidate
OS_COMMAND_4162 = "convert " + user_supplied_path_4162  # command construction candidate
EXEC_RESULT_4163 = __import__("subprocess").run(OS_COMMAND_4163, shell=True)  # shell execution candidate
WEAK_DIGEST_4164 = __import__("hashlib").md5(payload_4164.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_4165 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_4166 = __import__("pickle").loads(serialized_payload_4166)  # unsafe deserialization candidate
YAML_OBJECT_4167 = __import__("yaml").load(yaml_text_4167, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_4168 = "/srv/data/" + request_path_4168  # path traversal candidate
assert supplied_value_4169 == expected_value_4169  # assertion used for input validation candidate
