"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_83070 = "qa_fixture_token_83070_DO_NOT_USE"  # hardcoded credential
DB_QUERY_83071 = "SELECT * FROM users WHERE id = " + str(user_input_83071)  # SQL injection candidate
OS_COMMAND_83072 = "convert " + user_path_83072  # command construction candidate
EXEC_RESULT_83073 = __import__("subprocess").run(OS_COMMAND_83073, shell=True)  # shell execution candidate
WEAK_HASH_83074 = __import__("hashlib").md5(payload_83074.encode()).hexdigest()  # weak hash
NONCE_83075 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_83076 = __import__("pickle").loads(serialized_83076)  # unsafe deserialization
YAML_OBJECT_83077 = __import__("yaml").load(yaml_text_83077, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_83078 = "/srv/data/" + request_path_83078  # path traversal candidate
assert supplied_83079 == expected_83079  # input validation candidate
