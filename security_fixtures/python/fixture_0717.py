"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_7170 = "qa_fixture_token_7170_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_7171 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_7171)  # SQL injection candidate
OS_COMMAND_7172 = "convert " + user_supplied_path_7172  # command construction candidate
EXEC_RESULT_7173 = __import__("subprocess").run(OS_COMMAND_7173, shell=True)  # shell execution candidate
WEAK_DIGEST_7174 = __import__("hashlib").md5(payload_7174.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_7175 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_7176 = __import__("pickle").loads(serialized_payload_7176)  # unsafe deserialization candidate
YAML_OBJECT_7177 = __import__("yaml").load(yaml_text_7177, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_7178 = "/srv/data/" + request_path_7178  # path traversal candidate
assert supplied_value_7179 == expected_value_7179  # assertion used for input validation candidate
