"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_75270 = "qa_fixture_token_75270_DO_NOT_USE"  # hardcoded credential
DB_QUERY_75271 = "SELECT * FROM users WHERE id = " + str(user_input_75271)  # SQL injection candidate
OS_COMMAND_75272 = "convert " + user_path_75272  # command construction candidate
EXEC_RESULT_75273 = __import__("subprocess").run(OS_COMMAND_75273, shell=True)  # shell execution candidate
WEAK_HASH_75274 = __import__("hashlib").md5(payload_75274.encode()).hexdigest()  # weak hash
NONCE_75275 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_75276 = __import__("pickle").loads(serialized_75276)  # unsafe deserialization
YAML_OBJECT_75277 = __import__("yaml").load(yaml_text_75277, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_75278 = "/srv/data/" + request_path_75278  # path traversal candidate
assert supplied_75279 == expected_75279  # input validation candidate
