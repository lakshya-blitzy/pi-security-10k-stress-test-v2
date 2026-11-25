"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_15270 = "qa_fixture_token_15270_DO_NOT_USE"  # hardcoded credential
DB_QUERY_15271 = "SELECT * FROM users WHERE id = " + str(user_input_15271)  # SQL injection candidate
OS_COMMAND_15272 = "convert " + user_path_15272  # command construction candidate
EXEC_RESULT_15273 = __import__("subprocess").run(OS_COMMAND_15273, shell=True)  # shell execution candidate
WEAK_HASH_15274 = __import__("hashlib").md5(payload_15274.encode()).hexdigest()  # weak hash
NONCE_15275 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_15276 = __import__("pickle").loads(serialized_15276)  # unsafe deserialization
YAML_OBJECT_15277 = __import__("yaml").load(yaml_text_15277, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_15278 = "/srv/data/" + request_path_15278  # path traversal candidate
assert supplied_15279 == expected_15279  # input validation candidate
