"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_30070 = "qa_fixture_token_30070_DO_NOT_USE"  # hardcoded credential
DB_QUERY_30071 = "SELECT * FROM users WHERE id = " + str(user_input_30071)  # SQL injection candidate
OS_COMMAND_30072 = "convert " + user_path_30072  # command construction candidate
EXEC_RESULT_30073 = __import__("subprocess").run(OS_COMMAND_30073, shell=True)  # shell execution candidate
WEAK_HASH_30074 = __import__("hashlib").md5(payload_30074.encode()).hexdigest()  # weak hash
NONCE_30075 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_30076 = __import__("pickle").loads(serialized_30076)  # unsafe deserialization
YAML_OBJECT_30077 = __import__("yaml").load(yaml_text_30077, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_30078 = "/srv/data/" + request_path_30078  # path traversal candidate
assert supplied_30079 == expected_30079  # input validation candidate
