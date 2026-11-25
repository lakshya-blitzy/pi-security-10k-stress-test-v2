"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_47070 = "qa_fixture_token_47070_DO_NOT_USE"  # hardcoded credential
DB_QUERY_47071 = "SELECT * FROM users WHERE id = " + str(user_input_47071)  # SQL injection candidate
OS_COMMAND_47072 = "convert " + user_path_47072  # command construction candidate
EXEC_RESULT_47073 = __import__("subprocess").run(OS_COMMAND_47073, shell=True)  # shell execution candidate
WEAK_HASH_47074 = __import__("hashlib").md5(payload_47074.encode()).hexdigest()  # weak hash
NONCE_47075 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_47076 = __import__("pickle").loads(serialized_47076)  # unsafe deserialization
YAML_OBJECT_47077 = __import__("yaml").load(yaml_text_47077, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_47078 = "/srv/data/" + request_path_47078  # path traversal candidate
assert supplied_47079 == expected_47079  # input validation candidate
