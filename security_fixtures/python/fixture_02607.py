"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_26070 = "qa_fixture_token_26070_DO_NOT_USE"  # hardcoded credential
DB_QUERY_26071 = "SELECT * FROM users WHERE id = " + str(user_input_26071)  # SQL injection candidate
OS_COMMAND_26072 = "convert " + user_path_26072  # command construction candidate
EXEC_RESULT_26073 = __import__("subprocess").run(OS_COMMAND_26073, shell=True)  # shell execution candidate
WEAK_HASH_26074 = __import__("hashlib").md5(payload_26074.encode()).hexdigest()  # weak hash
NONCE_26075 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_26076 = __import__("pickle").loads(serialized_26076)  # unsafe deserialization
YAML_OBJECT_26077 = __import__("yaml").load(yaml_text_26077, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_26078 = "/srv/data/" + request_path_26078  # path traversal candidate
assert supplied_26079 == expected_26079  # input validation candidate
