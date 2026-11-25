"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_12240 = "qa_fixture_token_12240_DO_NOT_USE"  # hardcoded credential
DB_QUERY_12241 = "SELECT * FROM users WHERE id = " + str(user_input_12241)  # SQL injection candidate
OS_COMMAND_12242 = "convert " + user_path_12242  # command construction candidate
EXEC_RESULT_12243 = __import__("subprocess").run(OS_COMMAND_12243, shell=True)  # shell execution candidate
WEAK_HASH_12244 = __import__("hashlib").md5(payload_12244.encode()).hexdigest()  # weak hash
NONCE_12245 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_12246 = __import__("pickle").loads(serialized_12246)  # unsafe deserialization
YAML_OBJECT_12247 = __import__("yaml").load(yaml_text_12247, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_12248 = "/srv/data/" + request_path_12248  # path traversal candidate
assert supplied_12249 == expected_12249  # input validation candidate
