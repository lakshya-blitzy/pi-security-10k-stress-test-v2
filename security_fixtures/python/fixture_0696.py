"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_6960 = "qa_fixture_token_6960_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_6961 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_6961)  # SQL injection candidate
OS_COMMAND_6962 = "convert " + user_supplied_path_6962  # command construction candidate
EXEC_RESULT_6963 = __import__("subprocess").run(OS_COMMAND_6963, shell=True)  # shell execution candidate
WEAK_DIGEST_6964 = __import__("hashlib").md5(payload_6964.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_6965 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_6966 = __import__("pickle").loads(serialized_payload_6966)  # unsafe deserialization candidate
YAML_OBJECT_6967 = __import__("yaml").load(yaml_text_6967, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_6968 = "/srv/data/" + request_path_6968  # path traversal candidate
assert supplied_value_6969 == expected_value_6969  # assertion used for input validation candidate
