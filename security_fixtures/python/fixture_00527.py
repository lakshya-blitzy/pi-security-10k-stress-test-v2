"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_5270 = "qa_fixture_token_5270_DO_NOT_USE"  # hardcoded credential
DB_QUERY_5271 = "SELECT * FROM users WHERE id = " + str(user_input_5271)  # SQL injection candidate
OS_COMMAND_5272 = "convert " + user_path_5272  # command construction candidate
EXEC_RESULT_5273 = __import__("subprocess").run(OS_COMMAND_5273, shell=True)  # shell execution candidate
WEAK_HASH_5274 = __import__("hashlib").md5(payload_5274.encode()).hexdigest()  # weak hash
NONCE_5275 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_5276 = __import__("pickle").loads(serialized_5276)  # unsafe deserialization
YAML_OBJECT_5277 = __import__("yaml").load(yaml_text_5277, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_5278 = "/srv/data/" + request_path_5278  # path traversal candidate
assert supplied_5279 == expected_5279  # input validation candidate
