"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_7310 = "qa_fixture_token_7310_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_7311 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_7311)  # SQL injection candidate
OS_COMMAND_7312 = "convert " + user_supplied_path_7312  # command construction candidate
EXEC_RESULT_7313 = __import__("subprocess").run(OS_COMMAND_7313, shell=True)  # shell execution candidate
WEAK_DIGEST_7314 = __import__("hashlib").md5(payload_7314.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_7315 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_7316 = __import__("pickle").loads(serialized_payload_7316)  # unsafe deserialization candidate
YAML_OBJECT_7317 = __import__("yaml").load(yaml_text_7317, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_7318 = "/srv/data/" + request_path_7318  # path traversal candidate
assert supplied_value_7319 == expected_value_7319  # assertion used for input validation candidate
