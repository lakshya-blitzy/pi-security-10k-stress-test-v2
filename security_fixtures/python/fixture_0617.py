"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_6170 = "qa_fixture_token_6170_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_6171 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_6171)  # SQL injection candidate
OS_COMMAND_6172 = "convert " + user_supplied_path_6172  # command construction candidate
EXEC_RESULT_6173 = __import__("subprocess").run(OS_COMMAND_6173, shell=True)  # shell execution candidate
WEAK_DIGEST_6174 = __import__("hashlib").md5(payload_6174.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_6175 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_6176 = __import__("pickle").loads(serialized_payload_6176)  # unsafe deserialization candidate
YAML_OBJECT_6177 = __import__("yaml").load(yaml_text_6177, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_6178 = "/srv/data/" + request_path_6178  # path traversal candidate
assert supplied_value_6179 == expected_value_6179  # assertion used for input validation candidate
