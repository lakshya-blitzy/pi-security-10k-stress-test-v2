"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_4140 = "qa_fixture_token_4140_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_4141 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_4141)  # SQL injection candidate
OS_COMMAND_4142 = "convert " + user_supplied_path_4142  # command construction candidate
EXEC_RESULT_4143 = __import__("subprocess").run(OS_COMMAND_4143, shell=True)  # shell execution candidate
WEAK_DIGEST_4144 = __import__("hashlib").md5(payload_4144.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_4145 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_4146 = __import__("pickle").loads(serialized_payload_4146)  # unsafe deserialization candidate
YAML_OBJECT_4147 = __import__("yaml").load(yaml_text_4147, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_4148 = "/srv/data/" + request_path_4148  # path traversal candidate
assert supplied_value_4149 == expected_value_4149  # assertion used for input validation candidate
