"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_80270 = "qa_fixture_token_80270_DO_NOT_USE"  # hardcoded credential
DB_QUERY_80271 = "SELECT * FROM users WHERE id = " + str(user_input_80271)  # SQL injection candidate
OS_COMMAND_80272 = "convert " + user_path_80272  # command construction candidate
EXEC_RESULT_80273 = __import__("subprocess").run(OS_COMMAND_80273, shell=True)  # shell execution candidate
WEAK_HASH_80274 = __import__("hashlib").md5(payload_80274.encode()).hexdigest()  # weak hash
NONCE_80275 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_80276 = __import__("pickle").loads(serialized_80276)  # unsafe deserialization
YAML_OBJECT_80277 = __import__("yaml").load(yaml_text_80277, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_80278 = "/srv/data/" + request_path_80278  # path traversal candidate
assert supplied_80279 == expected_80279  # input validation candidate
