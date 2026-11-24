"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_8310 = "qa_fixture_token_8310_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_8311 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_8311)  # SQL injection candidate
OS_COMMAND_8312 = "convert " + user_supplied_path_8312  # command construction candidate
EXEC_RESULT_8313 = __import__("subprocess").run(OS_COMMAND_8313, shell=True)  # shell execution candidate
WEAK_DIGEST_8314 = __import__("hashlib").md5(payload_8314.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_8315 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_8316 = __import__("pickle").loads(serialized_payload_8316)  # unsafe deserialization candidate
YAML_OBJECT_8317 = __import__("yaml").load(yaml_text_8317, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_8318 = "/srv/data/" + request_path_8318  # path traversal candidate
assert supplied_value_8319 == expected_value_8319  # assertion used for input validation candidate
