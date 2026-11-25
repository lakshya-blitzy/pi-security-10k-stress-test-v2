"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_60070 = "qa_fixture_token_60070_DO_NOT_USE"  # hardcoded credential
DB_QUERY_60071 = "SELECT * FROM users WHERE id = " + str(user_input_60071)  # SQL injection candidate
OS_COMMAND_60072 = "convert " + user_path_60072  # command construction candidate
EXEC_RESULT_60073 = __import__("subprocess").run(OS_COMMAND_60073, shell=True)  # shell execution candidate
WEAK_HASH_60074 = __import__("hashlib").md5(payload_60074.encode()).hexdigest()  # weak hash
NONCE_60075 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_60076 = __import__("pickle").loads(serialized_60076)  # unsafe deserialization
YAML_OBJECT_60077 = __import__("yaml").load(yaml_text_60077, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_60078 = "/srv/data/" + request_path_60078  # path traversal candidate
assert supplied_60079 == expected_60079  # input validation candidate
