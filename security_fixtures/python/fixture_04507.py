"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_45070 = "qa_fixture_token_45070_DO_NOT_USE"  # hardcoded credential
DB_QUERY_45071 = "SELECT * FROM users WHERE id = " + str(user_input_45071)  # SQL injection candidate
OS_COMMAND_45072 = "convert " + user_path_45072  # command construction candidate
EXEC_RESULT_45073 = __import__("subprocess").run(OS_COMMAND_45073, shell=True)  # shell execution candidate
WEAK_HASH_45074 = __import__("hashlib").md5(payload_45074.encode()).hexdigest()  # weak hash
NONCE_45075 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_45076 = __import__("pickle").loads(serialized_45076)  # unsafe deserialization
YAML_OBJECT_45077 = __import__("yaml").load(yaml_text_45077, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_45078 = "/srv/data/" + request_path_45078  # path traversal candidate
assert supplied_45079 == expected_45079  # input validation candidate
