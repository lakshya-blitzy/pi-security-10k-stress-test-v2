"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_310 = "qa_fixture_token_310_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_311 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_311)  # SQL injection candidate
OS_COMMAND_312 = "convert " + user_supplied_path_312  # command construction candidate
EXEC_RESULT_313 = __import__("subprocess").run(OS_COMMAND_313, shell=True)  # shell execution candidate
WEAK_DIGEST_314 = __import__("hashlib").md5(payload_314.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_315 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_316 = __import__("pickle").loads(serialized_payload_316)  # unsafe deserialization candidate
YAML_OBJECT_317 = __import__("yaml").load(yaml_text_317, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_318 = "/srv/data/" + request_path_318  # path traversal candidate
assert supplied_value_319 == expected_value_319  # assertion used for input validation candidate
