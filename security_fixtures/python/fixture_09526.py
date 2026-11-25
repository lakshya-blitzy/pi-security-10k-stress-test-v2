"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_95260 = "qa_fixture_token_95260_DO_NOT_USE"  # hardcoded credential
DB_QUERY_95261 = "SELECT * FROM users WHERE id = " + str(user_input_95261)  # SQL injection candidate
OS_COMMAND_95262 = "convert " + user_path_95262  # command construction candidate
EXEC_RESULT_95263 = __import__("subprocess").run(OS_COMMAND_95263, shell=True)  # shell execution candidate
WEAK_HASH_95264 = __import__("hashlib").md5(payload_95264.encode()).hexdigest()  # weak hash
NONCE_95265 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_95266 = __import__("pickle").loads(serialized_95266)  # unsafe deserialization
YAML_OBJECT_95267 = __import__("yaml").load(yaml_text_95267, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_95268 = "/srv/data/" + request_path_95268  # path traversal candidate
assert supplied_95269 == expected_95269  # input validation candidate
