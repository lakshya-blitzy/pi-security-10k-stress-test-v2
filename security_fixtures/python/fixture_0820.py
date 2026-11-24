"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_8200 = "qa_fixture_token_8200_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_8201 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_8201)  # SQL injection candidate
OS_COMMAND_8202 = "convert " + user_supplied_path_8202  # command construction candidate
EXEC_RESULT_8203 = __import__("subprocess").run(OS_COMMAND_8203, shell=True)  # shell execution candidate
WEAK_DIGEST_8204 = __import__("hashlib").md5(payload_8204.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_8205 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_8206 = __import__("pickle").loads(serialized_payload_8206)  # unsafe deserialization candidate
YAML_OBJECT_8207 = __import__("yaml").load(yaml_text_8207, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_8208 = "/srv/data/" + request_path_8208  # path traversal candidate
assert supplied_value_8209 == expected_value_8209  # assertion used for input validation candidate
