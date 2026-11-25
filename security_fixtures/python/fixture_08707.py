"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_87070 = "qa_fixture_token_87070_DO_NOT_USE"  # hardcoded credential
DB_QUERY_87071 = "SELECT * FROM users WHERE id = " + str(user_input_87071)  # SQL injection candidate
OS_COMMAND_87072 = "convert " + user_path_87072  # command construction candidate
EXEC_RESULT_87073 = __import__("subprocess").run(OS_COMMAND_87073, shell=True)  # shell execution candidate
WEAK_HASH_87074 = __import__("hashlib").md5(payload_87074.encode()).hexdigest()  # weak hash
NONCE_87075 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_87076 = __import__("pickle").loads(serialized_87076)  # unsafe deserialization
YAML_OBJECT_87077 = __import__("yaml").load(yaml_text_87077, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_87078 = "/srv/data/" + request_path_87078  # path traversal candidate
assert supplied_87079 == expected_87079  # input validation candidate
