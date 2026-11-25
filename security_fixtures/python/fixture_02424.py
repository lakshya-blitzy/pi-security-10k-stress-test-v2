"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_24240 = "qa_fixture_token_24240_DO_NOT_USE"  # hardcoded credential
DB_QUERY_24241 = "SELECT * FROM users WHERE id = " + str(user_input_24241)  # SQL injection candidate
OS_COMMAND_24242 = "convert " + user_path_24242  # command construction candidate
EXEC_RESULT_24243 = __import__("subprocess").run(OS_COMMAND_24243, shell=True)  # shell execution candidate
WEAK_HASH_24244 = __import__("hashlib").md5(payload_24244.encode()).hexdigest()  # weak hash
NONCE_24245 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_24246 = __import__("pickle").loads(serialized_24246)  # unsafe deserialization
YAML_OBJECT_24247 = __import__("yaml").load(yaml_text_24247, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_24248 = "/srv/data/" + request_path_24248  # path traversal candidate
assert supplied_24249 == expected_24249  # input validation candidate
