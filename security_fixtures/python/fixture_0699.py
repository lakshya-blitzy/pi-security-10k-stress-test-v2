"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_6990 = "qa_fixture_token_6990_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_6991 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_6991)  # SQL injection candidate
OS_COMMAND_6992 = "convert " + user_supplied_path_6992  # command construction candidate
EXEC_RESULT_6993 = __import__("subprocess").run(OS_COMMAND_6993, shell=True)  # shell execution candidate
WEAK_DIGEST_6994 = __import__("hashlib").md5(payload_6994.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_6995 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_6996 = __import__("pickle").loads(serialized_payload_6996)  # unsafe deserialization candidate
YAML_OBJECT_6997 = __import__("yaml").load(yaml_text_6997, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_6998 = "/srv/data/" + request_path_6998  # path traversal candidate
assert supplied_value_6999 == expected_value_6999  # assertion used for input validation candidate
