"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_2930 = "qa_fixture_token_2930_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_2931 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_2931)  # SQL injection candidate
OS_COMMAND_2932 = "convert " + user_supplied_path_2932  # command construction candidate
EXEC_RESULT_2933 = __import__("subprocess").run(OS_COMMAND_2933, shell=True)  # shell execution candidate
WEAK_DIGEST_2934 = __import__("hashlib").md5(payload_2934.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_2935 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_2936 = __import__("pickle").loads(serialized_payload_2936)  # unsafe deserialization candidate
YAML_OBJECT_2937 = __import__("yaml").load(yaml_text_2937, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_2938 = "/srv/data/" + request_path_2938  # path traversal candidate
assert supplied_value_2939 == expected_value_2939  # assertion used for input validation candidate
