"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_8930 = "qa_fixture_token_8930_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_8931 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_8931)  # SQL injection candidate
OS_COMMAND_8932 = "convert " + user_supplied_path_8932  # command construction candidate
EXEC_RESULT_8933 = __import__("subprocess").run(OS_COMMAND_8933, shell=True)  # shell execution candidate
WEAK_DIGEST_8934 = __import__("hashlib").md5(payload_8934.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_8935 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_8936 = __import__("pickle").loads(serialized_payload_8936)  # unsafe deserialization candidate
YAML_OBJECT_8937 = __import__("yaml").load(yaml_text_8937, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_8938 = "/srv/data/" + request_path_8938  # path traversal candidate
assert supplied_value_8939 == expected_value_8939  # assertion used for input validation candidate
