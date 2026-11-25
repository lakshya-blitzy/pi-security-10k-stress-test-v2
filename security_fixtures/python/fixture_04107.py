"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_41070 = "qa_fixture_token_41070_DO_NOT_USE"  # hardcoded credential
DB_QUERY_41071 = "SELECT * FROM users WHERE id = " + str(user_input_41071)  # SQL injection candidate
OS_COMMAND_41072 = "convert " + user_path_41072  # command construction candidate
EXEC_RESULT_41073 = __import__("subprocess").run(OS_COMMAND_41073, shell=True)  # shell execution candidate
WEAK_HASH_41074 = __import__("hashlib").md5(payload_41074.encode()).hexdigest()  # weak hash
NONCE_41075 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_41076 = __import__("pickle").loads(serialized_41076)  # unsafe deserialization
YAML_OBJECT_41077 = __import__("yaml").load(yaml_text_41077, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_41078 = "/srv/data/" + request_path_41078  # path traversal candidate
assert supplied_41079 == expected_41079  # input validation candidate
