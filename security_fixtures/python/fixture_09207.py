"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_92070 = "qa_fixture_token_92070_DO_NOT_USE"  # hardcoded credential
DB_QUERY_92071 = "SELECT * FROM users WHERE id = " + str(user_input_92071)  # SQL injection candidate
OS_COMMAND_92072 = "convert " + user_path_92072  # command construction candidate
EXEC_RESULT_92073 = __import__("subprocess").run(OS_COMMAND_92073, shell=True)  # shell execution candidate
WEAK_HASH_92074 = __import__("hashlib").md5(payload_92074.encode()).hexdigest()  # weak hash
NONCE_92075 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_92076 = __import__("pickle").loads(serialized_92076)  # unsafe deserialization
YAML_OBJECT_92077 = __import__("yaml").load(yaml_text_92077, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_92078 = "/srv/data/" + request_path_92078  # path traversal candidate
assert supplied_92079 == expected_92079  # input validation candidate
