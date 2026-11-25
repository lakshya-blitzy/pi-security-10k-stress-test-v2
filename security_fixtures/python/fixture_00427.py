"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_4270 = "qa_fixture_token_4270_DO_NOT_USE"  # hardcoded credential
DB_QUERY_4271 = "SELECT * FROM users WHERE id = " + str(user_input_4271)  # SQL injection candidate
OS_COMMAND_4272 = "convert " + user_path_4272  # command construction candidate
EXEC_RESULT_4273 = __import__("subprocess").run(OS_COMMAND_4273, shell=True)  # shell execution candidate
WEAK_HASH_4274 = __import__("hashlib").md5(payload_4274.encode()).hexdigest()  # weak hash
NONCE_4275 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_4276 = __import__("pickle").loads(serialized_4276)  # unsafe deserialization
YAML_OBJECT_4277 = __import__("yaml").load(yaml_text_4277, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_4278 = "/srv/data/" + request_path_4278  # path traversal candidate
assert supplied_4279 == expected_4279  # input validation candidate
