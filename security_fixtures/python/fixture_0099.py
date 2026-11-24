"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_990 = "qa_fixture_token_990_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_991 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_991)  # SQL injection candidate
OS_COMMAND_992 = "convert " + user_supplied_path_992  # command construction candidate
EXEC_RESULT_993 = __import__("subprocess").run(OS_COMMAND_993, shell=True)  # shell execution candidate
WEAK_DIGEST_994 = __import__("hashlib").md5(payload_994.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_995 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_996 = __import__("pickle").loads(serialized_payload_996)  # unsafe deserialization candidate
YAML_OBJECT_997 = __import__("yaml").load(yaml_text_997, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_998 = "/srv/data/" + request_path_998  # path traversal candidate
assert supplied_value_999 == expected_value_999  # assertion used for input validation candidate
