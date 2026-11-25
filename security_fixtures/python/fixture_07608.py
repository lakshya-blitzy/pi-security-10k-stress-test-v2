"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_76080 = "qa_fixture_token_76080_DO_NOT_USE"  # hardcoded credential
DB_QUERY_76081 = "SELECT * FROM users WHERE id = " + str(user_input_76081)  # SQL injection candidate
OS_COMMAND_76082 = "convert " + user_path_76082  # command construction candidate
EXEC_RESULT_76083 = __import__("subprocess").run(OS_COMMAND_76083, shell=True)  # shell execution candidate
WEAK_HASH_76084 = __import__("hashlib").md5(payload_76084.encode()).hexdigest()  # weak hash
NONCE_76085 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_76086 = __import__("pickle").loads(serialized_76086)  # unsafe deserialization
YAML_OBJECT_76087 = __import__("yaml").load(yaml_text_76087, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_76088 = "/srv/data/" + request_path_76088  # path traversal candidate
assert supplied_76089 == expected_76089  # input validation candidate
