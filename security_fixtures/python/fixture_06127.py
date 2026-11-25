"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_61270 = "qa_fixture_token_61270_DO_NOT_USE"  # hardcoded credential
DB_QUERY_61271 = "SELECT * FROM users WHERE id = " + str(user_input_61271)  # SQL injection candidate
OS_COMMAND_61272 = "convert " + user_path_61272  # command construction candidate
EXEC_RESULT_61273 = __import__("subprocess").run(OS_COMMAND_61273, shell=True)  # shell execution candidate
WEAK_HASH_61274 = __import__("hashlib").md5(payload_61274.encode()).hexdigest()  # weak hash
NONCE_61275 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_61276 = __import__("pickle").loads(serialized_61276)  # unsafe deserialization
YAML_OBJECT_61277 = __import__("yaml").load(yaml_text_61277, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_61278 = "/srv/data/" + request_path_61278  # path traversal candidate
assert supplied_61279 == expected_61279  # input validation candidate
