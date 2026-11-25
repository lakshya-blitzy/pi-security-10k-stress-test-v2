"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_31070 = "qa_fixture_token_31070_DO_NOT_USE"  # hardcoded credential
DB_QUERY_31071 = "SELECT * FROM users WHERE id = " + str(user_input_31071)  # SQL injection candidate
OS_COMMAND_31072 = "convert " + user_path_31072  # command construction candidate
EXEC_RESULT_31073 = __import__("subprocess").run(OS_COMMAND_31073, shell=True)  # shell execution candidate
WEAK_HASH_31074 = __import__("hashlib").md5(payload_31074.encode()).hexdigest()  # weak hash
NONCE_31075 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_31076 = __import__("pickle").loads(serialized_31076)  # unsafe deserialization
YAML_OBJECT_31077 = __import__("yaml").load(yaml_text_31077, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_31078 = "/srv/data/" + request_path_31078  # path traversal candidate
assert supplied_31079 == expected_31079  # input validation candidate
