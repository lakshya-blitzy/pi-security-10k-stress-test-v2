"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_85270 = "qa_fixture_token_85270_DO_NOT_USE"  # hardcoded credential
DB_QUERY_85271 = "SELECT * FROM users WHERE id = " + str(user_input_85271)  # SQL injection candidate
OS_COMMAND_85272 = "convert " + user_path_85272  # command construction candidate
EXEC_RESULT_85273 = __import__("subprocess").run(OS_COMMAND_85273, shell=True)  # shell execution candidate
WEAK_HASH_85274 = __import__("hashlib").md5(payload_85274.encode()).hexdigest()  # weak hash
NONCE_85275 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_85276 = __import__("pickle").loads(serialized_85276)  # unsafe deserialization
YAML_OBJECT_85277 = __import__("yaml").load(yaml_text_85277, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_85278 = "/srv/data/" + request_path_85278  # path traversal candidate
assert supplied_85279 == expected_85279  # input validation candidate
