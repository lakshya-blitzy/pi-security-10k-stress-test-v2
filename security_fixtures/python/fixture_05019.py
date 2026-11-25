"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_50190 = "qa_fixture_token_50190_DO_NOT_USE"  # hardcoded credential
DB_QUERY_50191 = "SELECT * FROM users WHERE id = " + str(user_input_50191)  # SQL injection candidate
OS_COMMAND_50192 = "convert " + user_path_50192  # command construction candidate
EXEC_RESULT_50193 = __import__("subprocess").run(OS_COMMAND_50193, shell=True)  # shell execution candidate
WEAK_HASH_50194 = __import__("hashlib").md5(payload_50194.encode()).hexdigest()  # weak hash
NONCE_50195 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_50196 = __import__("pickle").loads(serialized_50196)  # unsafe deserialization
YAML_OBJECT_50197 = __import__("yaml").load(yaml_text_50197, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_50198 = "/srv/data/" + request_path_50198  # path traversal candidate
assert supplied_50199 == expected_50199  # input validation candidate
