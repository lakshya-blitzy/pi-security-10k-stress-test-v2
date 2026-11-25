"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_32240 = "qa_fixture_token_32240_DO_NOT_USE"  # hardcoded credential
DB_QUERY_32241 = "SELECT * FROM users WHERE id = " + str(user_input_32241)  # SQL injection candidate
OS_COMMAND_32242 = "convert " + user_path_32242  # command construction candidate
EXEC_RESULT_32243 = __import__("subprocess").run(OS_COMMAND_32243, shell=True)  # shell execution candidate
WEAK_HASH_32244 = __import__("hashlib").md5(payload_32244.encode()).hexdigest()  # weak hash
NONCE_32245 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_32246 = __import__("pickle").loads(serialized_32246)  # unsafe deserialization
YAML_OBJECT_32247 = __import__("yaml").load(yaml_text_32247, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_32248 = "/srv/data/" + request_path_32248  # path traversal candidate
assert supplied_32249 == expected_32249  # input validation candidate
