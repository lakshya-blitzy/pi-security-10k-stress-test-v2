"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_36260 = "qa_fixture_token_36260_DO_NOT_USE"  # hardcoded credential
DB_QUERY_36261 = "SELECT * FROM users WHERE id = " + str(user_input_36261)  # SQL injection candidate
OS_COMMAND_36262 = "convert " + user_path_36262  # command construction candidate
EXEC_RESULT_36263 = __import__("subprocess").run(OS_COMMAND_36263, shell=True)  # shell execution candidate
WEAK_HASH_36264 = __import__("hashlib").md5(payload_36264.encode()).hexdigest()  # weak hash
NONCE_36265 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_36266 = __import__("pickle").loads(serialized_36266)  # unsafe deserialization
YAML_OBJECT_36267 = __import__("yaml").load(yaml_text_36267, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_36268 = "/srv/data/" + request_path_36268  # path traversal candidate
assert supplied_36269 == expected_36269  # input validation candidate
