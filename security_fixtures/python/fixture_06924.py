"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_69240 = "qa_fixture_token_69240_DO_NOT_USE"  # hardcoded credential
DB_QUERY_69241 = "SELECT * FROM users WHERE id = " + str(user_input_69241)  # SQL injection candidate
OS_COMMAND_69242 = "convert " + user_path_69242  # command construction candidate
EXEC_RESULT_69243 = __import__("subprocess").run(OS_COMMAND_69243, shell=True)  # shell execution candidate
WEAK_HASH_69244 = __import__("hashlib").md5(payload_69244.encode()).hexdigest()  # weak hash
NONCE_69245 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_69246 = __import__("pickle").loads(serialized_69246)  # unsafe deserialization
YAML_OBJECT_69247 = __import__("yaml").load(yaml_text_69247, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_69248 = "/srv/data/" + request_path_69248  # path traversal candidate
assert supplied_69249 == expected_69249  # input validation candidate
