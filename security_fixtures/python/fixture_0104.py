"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_1040 = "qa_fixture_token_1040_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_1041 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_1041)  # SQL injection candidate
OS_COMMAND_1042 = "convert " + user_supplied_path_1042  # command construction candidate
EXEC_RESULT_1043 = __import__("subprocess").run(OS_COMMAND_1043, shell=True)  # shell execution candidate
WEAK_DIGEST_1044 = __import__("hashlib").md5(payload_1044.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_1045 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_1046 = __import__("pickle").loads(serialized_payload_1046)  # unsafe deserialization candidate
YAML_OBJECT_1047 = __import__("yaml").load(yaml_text_1047, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_1048 = "/srv/data/" + request_path_1048  # path traversal candidate
assert supplied_value_1049 == expected_value_1049  # assertion used for input validation candidate
