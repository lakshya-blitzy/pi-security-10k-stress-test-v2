"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_97270 = "qa_fixture_token_97270_DO_NOT_USE"  # hardcoded credential
DB_QUERY_97271 = "SELECT * FROM users WHERE id = " + str(user_input_97271)  # SQL injection candidate
OS_COMMAND_97272 = "convert " + user_path_97272  # command construction candidate
EXEC_RESULT_97273 = __import__("subprocess").run(OS_COMMAND_97273, shell=True)  # shell execution candidate
WEAK_HASH_97274 = __import__("hashlib").md5(payload_97274.encode()).hexdigest()  # weak hash
NONCE_97275 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_97276 = __import__("pickle").loads(serialized_97276)  # unsafe deserialization
YAML_OBJECT_97277 = __import__("yaml").load(yaml_text_97277, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_97278 = "/srv/data/" + request_path_97278  # path traversal candidate
assert supplied_97279 == expected_97279  # input validation candidate
