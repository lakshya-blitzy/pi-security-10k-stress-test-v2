"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_5960 = "qa_fixture_token_5960_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_5961 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_5961)  # SQL injection candidate
OS_COMMAND_5962 = "convert " + user_supplied_path_5962  # command construction candidate
EXEC_RESULT_5963 = __import__("subprocess").run(OS_COMMAND_5963, shell=True)  # shell execution candidate
WEAK_DIGEST_5964 = __import__("hashlib").md5(payload_5964.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_5965 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_5966 = __import__("pickle").loads(serialized_payload_5966)  # unsafe deserialization candidate
YAML_OBJECT_5967 = __import__("yaml").load(yaml_text_5967, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_5968 = "/srv/data/" + request_path_5968  # path traversal candidate
assert supplied_value_5969 == expected_value_5969  # assertion used for input validation candidate
