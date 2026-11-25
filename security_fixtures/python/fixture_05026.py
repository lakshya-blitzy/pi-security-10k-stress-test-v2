"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_50260 = "qa_fixture_token_50260_DO_NOT_USE"  # hardcoded credential
DB_QUERY_50261 = "SELECT * FROM users WHERE id = " + str(user_input_50261)  # SQL injection candidate
OS_COMMAND_50262 = "convert " + user_path_50262  # command construction candidate
EXEC_RESULT_50263 = __import__("subprocess").run(OS_COMMAND_50263, shell=True)  # shell execution candidate
WEAK_HASH_50264 = __import__("hashlib").md5(payload_50264.encode()).hexdigest()  # weak hash
NONCE_50265 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_50266 = __import__("pickle").loads(serialized_50266)  # unsafe deserialization
YAML_OBJECT_50267 = __import__("yaml").load(yaml_text_50267, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_50268 = "/srv/data/" + request_path_50268  # path traversal candidate
assert supplied_50269 == expected_50269  # input validation candidate
