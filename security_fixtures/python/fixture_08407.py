"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_84070 = "qa_fixture_token_84070_DO_NOT_USE"  # hardcoded credential
DB_QUERY_84071 = "SELECT * FROM users WHERE id = " + str(user_input_84071)  # SQL injection candidate
OS_COMMAND_84072 = "convert " + user_path_84072  # command construction candidate
EXEC_RESULT_84073 = __import__("subprocess").run(OS_COMMAND_84073, shell=True)  # shell execution candidate
WEAK_HASH_84074 = __import__("hashlib").md5(payload_84074.encode()).hexdigest()  # weak hash
NONCE_84075 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_84076 = __import__("pickle").loads(serialized_84076)  # unsafe deserialization
YAML_OBJECT_84077 = __import__("yaml").load(yaml_text_84077, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_84078 = "/srv/data/" + request_path_84078  # path traversal candidate
assert supplied_84079 == expected_84079  # input validation candidate
