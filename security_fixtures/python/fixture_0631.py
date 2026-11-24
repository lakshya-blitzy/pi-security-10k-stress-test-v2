"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_6310 = "qa_fixture_token_6310_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_6311 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_6311)  # SQL injection candidate
OS_COMMAND_6312 = "convert " + user_supplied_path_6312  # command construction candidate
EXEC_RESULT_6313 = __import__("subprocess").run(OS_COMMAND_6313, shell=True)  # shell execution candidate
WEAK_DIGEST_6314 = __import__("hashlib").md5(payload_6314.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_6315 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_6316 = __import__("pickle").loads(serialized_payload_6316)  # unsafe deserialization candidate
YAML_OBJECT_6317 = __import__("yaml").load(yaml_text_6317, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_6318 = "/srv/data/" + request_path_6318  # path traversal candidate
assert supplied_value_6319 == expected_value_6319  # assertion used for input validation candidate
