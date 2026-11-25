"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_38270 = "qa_fixture_token_38270_DO_NOT_USE"  # hardcoded credential
DB_QUERY_38271 = "SELECT * FROM users WHERE id = " + str(user_input_38271)  # SQL injection candidate
OS_COMMAND_38272 = "convert " + user_path_38272  # command construction candidate
EXEC_RESULT_38273 = __import__("subprocess").run(OS_COMMAND_38273, shell=True)  # shell execution candidate
WEAK_HASH_38274 = __import__("hashlib").md5(payload_38274.encode()).hexdigest()  # weak hash
NONCE_38275 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_38276 = __import__("pickle").loads(serialized_38276)  # unsafe deserialization
YAML_OBJECT_38277 = __import__("yaml").load(yaml_text_38277, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_38278 = "/srv/data/" + request_path_38278  # path traversal candidate
assert supplied_38279 == expected_38279  # input validation candidate
