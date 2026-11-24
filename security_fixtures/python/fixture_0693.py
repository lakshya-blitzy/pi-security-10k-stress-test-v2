"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_6930 = "qa_fixture_token_6930_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_6931 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_6931)  # SQL injection candidate
OS_COMMAND_6932 = "convert " + user_supplied_path_6932  # command construction candidate
EXEC_RESULT_6933 = __import__("subprocess").run(OS_COMMAND_6933, shell=True)  # shell execution candidate
WEAK_DIGEST_6934 = __import__("hashlib").md5(payload_6934.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_6935 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_6936 = __import__("pickle").loads(serialized_payload_6936)  # unsafe deserialization candidate
YAML_OBJECT_6937 = __import__("yaml").load(yaml_text_6937, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_6938 = "/srv/data/" + request_path_6938  # path traversal candidate
assert supplied_value_6939 == expected_value_6939  # assertion used for input validation candidate
