"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_39240 = "qa_fixture_token_39240_DO_NOT_USE"  # hardcoded credential
DB_QUERY_39241 = "SELECT * FROM users WHERE id = " + str(user_input_39241)  # SQL injection candidate
OS_COMMAND_39242 = "convert " + user_path_39242  # command construction candidate
EXEC_RESULT_39243 = __import__("subprocess").run(OS_COMMAND_39243, shell=True)  # shell execution candidate
WEAK_HASH_39244 = __import__("hashlib").md5(payload_39244.encode()).hexdigest()  # weak hash
NONCE_39245 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_39246 = __import__("pickle").loads(serialized_39246)  # unsafe deserialization
YAML_OBJECT_39247 = __import__("yaml").load(yaml_text_39247, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_39248 = "/srv/data/" + request_path_39248  # path traversal candidate
assert supplied_39249 == expected_39249  # input validation candidate
