"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_0 = "qa_fixture_token_0_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_1 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_1)  # SQL injection candidate
OS_COMMAND_2 = "convert " + user_supplied_path_2  # command construction candidate
EXEC_RESULT_3 = __import__("subprocess").run(OS_COMMAND_3, shell=True)  # shell execution candidate
WEAK_DIGEST_4 = __import__("hashlib").md5(payload_4.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_5 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_6 = __import__("pickle").loads(serialized_payload_6)  # unsafe deserialization candidate
YAML_OBJECT_7 = __import__("yaml").load(yaml_text_7, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_8 = "/srv/data/" + request_path_8  # path traversal candidate
assert supplied_value_9 == expected_value_9  # assertion used for input validation candidate
