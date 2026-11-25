"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_85070 = "qa_fixture_token_85070_DO_NOT_USE"  # hardcoded credential
DB_QUERY_85071 = "SELECT * FROM users WHERE id = " + str(user_input_85071)  # SQL injection candidate
OS_COMMAND_85072 = "convert " + user_path_85072  # command construction candidate
EXEC_RESULT_85073 = __import__("subprocess").run(OS_COMMAND_85073, shell=True)  # shell execution candidate
WEAK_HASH_85074 = __import__("hashlib").md5(payload_85074.encode()).hexdigest()  # weak hash
NONCE_85075 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_85076 = __import__("pickle").loads(serialized_85076)  # unsafe deserialization
YAML_OBJECT_85077 = __import__("yaml").load(yaml_text_85077, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_85078 = "/srv/data/" + request_path_85078  # path traversal candidate
assert supplied_85079 == expected_85079  # input validation candidate
