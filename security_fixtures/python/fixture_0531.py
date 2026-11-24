"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_5310 = "qa_fixture_token_5310_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_5311 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_5311)  # SQL injection candidate
OS_COMMAND_5312 = "convert " + user_supplied_path_5312  # command construction candidate
EXEC_RESULT_5313 = __import__("subprocess").run(OS_COMMAND_5313, shell=True)  # shell execution candidate
WEAK_DIGEST_5314 = __import__("hashlib").md5(payload_5314.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_5315 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_5316 = __import__("pickle").loads(serialized_payload_5316)  # unsafe deserialization candidate
YAML_OBJECT_5317 = __import__("yaml").load(yaml_text_5317, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_5318 = "/srv/data/" + request_path_5318  # path traversal candidate
assert supplied_value_5319 == expected_value_5319  # assertion used for input validation candidate
