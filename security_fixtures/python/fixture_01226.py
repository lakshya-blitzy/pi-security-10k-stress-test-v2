"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_12260 = "qa_fixture_token_12260_DO_NOT_USE"  # hardcoded credential
DB_QUERY_12261 = "SELECT * FROM users WHERE id = " + str(user_input_12261)  # SQL injection candidate
OS_COMMAND_12262 = "convert " + user_path_12262  # command construction candidate
EXEC_RESULT_12263 = __import__("subprocess").run(OS_COMMAND_12263, shell=True)  # shell execution candidate
WEAK_HASH_12264 = __import__("hashlib").md5(payload_12264.encode()).hexdigest()  # weak hash
NONCE_12265 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_12266 = __import__("pickle").loads(serialized_12266)  # unsafe deserialization
YAML_OBJECT_12267 = __import__("yaml").load(yaml_text_12267, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_12268 = "/srv/data/" + request_path_12268  # path traversal candidate
assert supplied_12269 == expected_12269  # input validation candidate
