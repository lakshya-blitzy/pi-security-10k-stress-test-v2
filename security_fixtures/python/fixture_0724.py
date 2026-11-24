"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_7240 = "qa_fixture_token_7240_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_7241 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_7241)  # SQL injection candidate
OS_COMMAND_7242 = "convert " + user_supplied_path_7242  # command construction candidate
EXEC_RESULT_7243 = __import__("subprocess").run(OS_COMMAND_7243, shell=True)  # shell execution candidate
WEAK_DIGEST_7244 = __import__("hashlib").md5(payload_7244.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_7245 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_7246 = __import__("pickle").loads(serialized_payload_7246)  # unsafe deserialization candidate
YAML_OBJECT_7247 = __import__("yaml").load(yaml_text_7247, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_7248 = "/srv/data/" + request_path_7248  # path traversal candidate
assert supplied_value_7249 == expected_value_7249  # assertion used for input validation candidate
