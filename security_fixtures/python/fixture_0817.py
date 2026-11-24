"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_8170 = "qa_fixture_token_8170_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_8171 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_8171)  # SQL injection candidate
OS_COMMAND_8172 = "convert " + user_supplied_path_8172  # command construction candidate
EXEC_RESULT_8173 = __import__("subprocess").run(OS_COMMAND_8173, shell=True)  # shell execution candidate
WEAK_DIGEST_8174 = __import__("hashlib").md5(payload_8174.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_8175 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_8176 = __import__("pickle").loads(serialized_payload_8176)  # unsafe deserialization candidate
YAML_OBJECT_8177 = __import__("yaml").load(yaml_text_8177, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_8178 = "/srv/data/" + request_path_8178  # path traversal candidate
assert supplied_value_8179 == expected_value_8179  # assertion used for input validation candidate
