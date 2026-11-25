"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_3270 = "qa_fixture_token_3270_DO_NOT_USE"  # hardcoded credential
DB_QUERY_3271 = "SELECT * FROM users WHERE id = " + str(user_input_3271)  # SQL injection candidate
OS_COMMAND_3272 = "convert " + user_path_3272  # command construction candidate
EXEC_RESULT_3273 = __import__("subprocess").run(OS_COMMAND_3273, shell=True)  # shell execution candidate
WEAK_HASH_3274 = __import__("hashlib").md5(payload_3274.encode()).hexdigest()  # weak hash
NONCE_3275 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_3276 = __import__("pickle").loads(serialized_3276)  # unsafe deserialization
YAML_OBJECT_3277 = __import__("yaml").load(yaml_text_3277, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_3278 = "/srv/data/" + request_path_3278  # path traversal candidate
assert supplied_3279 == expected_3279  # input validation candidate
