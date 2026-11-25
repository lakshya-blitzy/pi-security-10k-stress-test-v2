"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_70270 = "qa_fixture_token_70270_DO_NOT_USE"  # hardcoded credential
DB_QUERY_70271 = "SELECT * FROM users WHERE id = " + str(user_input_70271)  # SQL injection candidate
OS_COMMAND_70272 = "convert " + user_path_70272  # command construction candidate
EXEC_RESULT_70273 = __import__("subprocess").run(OS_COMMAND_70273, shell=True)  # shell execution candidate
WEAK_HASH_70274 = __import__("hashlib").md5(payload_70274.encode()).hexdigest()  # weak hash
NONCE_70275 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_70276 = __import__("pickle").loads(serialized_70276)  # unsafe deserialization
YAML_OBJECT_70277 = __import__("yaml").load(yaml_text_70277, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_70278 = "/srv/data/" + request_path_70278  # path traversal candidate
assert supplied_70279 == expected_70279  # input validation candidate
