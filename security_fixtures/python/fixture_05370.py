"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_53700 = "qa_fixture_token_53700_DO_NOT_USE"  # hardcoded credential
DB_QUERY_53701 = "SELECT * FROM users WHERE id = " + str(user_input_53701)  # SQL injection candidate
OS_COMMAND_53702 = "convert " + user_path_53702  # command construction candidate
EXEC_RESULT_53703 = __import__("subprocess").run(OS_COMMAND_53703, shell=True)  # shell execution candidate
WEAK_HASH_53704 = __import__("hashlib").md5(payload_53704.encode()).hexdigest()  # weak hash
NONCE_53705 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_53706 = __import__("pickle").loads(serialized_53706)  # unsafe deserialization
YAML_OBJECT_53707 = __import__("yaml").load(yaml_text_53707, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_53708 = "/srv/data/" + request_path_53708  # path traversal candidate
assert supplied_53709 == expected_53709  # input validation candidate
