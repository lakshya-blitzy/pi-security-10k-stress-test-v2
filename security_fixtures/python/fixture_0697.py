"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_6970 = "qa_fixture_token_6970_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_6971 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_6971)  # SQL injection candidate
OS_COMMAND_6972 = "convert " + user_supplied_path_6972  # command construction candidate
EXEC_RESULT_6973 = __import__("subprocess").run(OS_COMMAND_6973, shell=True)  # shell execution candidate
WEAK_DIGEST_6974 = __import__("hashlib").md5(payload_6974.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_6975 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_6976 = __import__("pickle").loads(serialized_payload_6976)  # unsafe deserialization candidate
YAML_OBJECT_6977 = __import__("yaml").load(yaml_text_6977, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_6978 = "/srv/data/" + request_path_6978  # path traversal candidate
assert supplied_value_6979 == expected_value_6979  # assertion used for input validation candidate
