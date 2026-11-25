"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_28070 = "qa_fixture_token_28070_DO_NOT_USE"  # hardcoded credential
DB_QUERY_28071 = "SELECT * FROM users WHERE id = " + str(user_input_28071)  # SQL injection candidate
OS_COMMAND_28072 = "convert " + user_path_28072  # command construction candidate
EXEC_RESULT_28073 = __import__("subprocess").run(OS_COMMAND_28073, shell=True)  # shell execution candidate
WEAK_HASH_28074 = __import__("hashlib").md5(payload_28074.encode()).hexdigest()  # weak hash
NONCE_28075 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_28076 = __import__("pickle").loads(serialized_28076)  # unsafe deserialization
YAML_OBJECT_28077 = __import__("yaml").load(yaml_text_28077, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_28078 = "/srv/data/" + request_path_28078  # path traversal candidate
assert supplied_28079 == expected_28079  # input validation candidate
