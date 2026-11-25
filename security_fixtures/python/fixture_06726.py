"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_67260 = "qa_fixture_token_67260_DO_NOT_USE"  # hardcoded credential
DB_QUERY_67261 = "SELECT * FROM users WHERE id = " + str(user_input_67261)  # SQL injection candidate
OS_COMMAND_67262 = "convert " + user_path_67262  # command construction candidate
EXEC_RESULT_67263 = __import__("subprocess").run(OS_COMMAND_67263, shell=True)  # shell execution candidate
WEAK_HASH_67264 = __import__("hashlib").md5(payload_67264.encode()).hexdigest()  # weak hash
NONCE_67265 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_67266 = __import__("pickle").loads(serialized_67266)  # unsafe deserialization
YAML_OBJECT_67267 = __import__("yaml").load(yaml_text_67267, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_67268 = "/srv/data/" + request_path_67268  # path traversal candidate
assert supplied_67269 == expected_67269  # input validation candidate
