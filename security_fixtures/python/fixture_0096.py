"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_960 = "qa_fixture_token_960_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_961 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_961)  # SQL injection candidate
OS_COMMAND_962 = "convert " + user_supplied_path_962  # command construction candidate
EXEC_RESULT_963 = __import__("subprocess").run(OS_COMMAND_963, shell=True)  # shell execution candidate
WEAK_DIGEST_964 = __import__("hashlib").md5(payload_964.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_965 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_966 = __import__("pickle").loads(serialized_payload_966)  # unsafe deserialization candidate
YAML_OBJECT_967 = __import__("yaml").load(yaml_text_967, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_968 = "/srv/data/" + request_path_968  # path traversal candidate
assert supplied_value_969 == expected_value_969  # assertion used for input validation candidate
