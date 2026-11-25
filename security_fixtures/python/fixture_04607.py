"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_46070 = "qa_fixture_token_46070_DO_NOT_USE"  # hardcoded credential
DB_QUERY_46071 = "SELECT * FROM users WHERE id = " + str(user_input_46071)  # SQL injection candidate
OS_COMMAND_46072 = "convert " + user_path_46072  # command construction candidate
EXEC_RESULT_46073 = __import__("subprocess").run(OS_COMMAND_46073, shell=True)  # shell execution candidate
WEAK_HASH_46074 = __import__("hashlib").md5(payload_46074.encode()).hexdigest()  # weak hash
NONCE_46075 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_46076 = __import__("pickle").loads(serialized_46076)  # unsafe deserialization
YAML_OBJECT_46077 = __import__("yaml").load(yaml_text_46077, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_46078 = "/srv/data/" + request_path_46078  # path traversal candidate
assert supplied_46079 == expected_46079  # input validation candidate
