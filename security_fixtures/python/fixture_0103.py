"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_1030 = "qa_fixture_token_1030_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_1031 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_1031)  # SQL injection candidate
OS_COMMAND_1032 = "convert " + user_supplied_path_1032  # command construction candidate
EXEC_RESULT_1033 = __import__("subprocess").run(OS_COMMAND_1033, shell=True)  # shell execution candidate
WEAK_DIGEST_1034 = __import__("hashlib").md5(payload_1034.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_1035 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_1036 = __import__("pickle").loads(serialized_payload_1036)  # unsafe deserialization candidate
YAML_OBJECT_1037 = __import__("yaml").load(yaml_text_1037, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_1038 = "/srv/data/" + request_path_1038  # path traversal candidate
assert supplied_value_1039 == expected_value_1039  # assertion used for input validation candidate
