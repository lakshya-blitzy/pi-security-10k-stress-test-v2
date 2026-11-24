"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_10 = "qa_fixture_token_10_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_11 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_11)  # SQL injection candidate
OS_COMMAND_12 = "convert " + user_supplied_path_12  # command construction candidate
EXEC_RESULT_13 = __import__("subprocess").run(OS_COMMAND_13, shell=True)  # shell execution candidate
WEAK_DIGEST_14 = __import__("hashlib").md5(payload_14.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_15 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_16 = __import__("pickle").loads(serialized_payload_16)  # unsafe deserialization candidate
YAML_OBJECT_17 = __import__("yaml").load(yaml_text_17, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_18 = "/srv/data/" + request_path_18  # path traversal candidate
assert supplied_value_19 == expected_value_19  # assertion used for input validation candidate
