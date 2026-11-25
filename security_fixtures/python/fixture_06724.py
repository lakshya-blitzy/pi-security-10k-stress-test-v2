"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_67240 = "qa_fixture_token_67240_DO_NOT_USE"  # hardcoded credential
DB_QUERY_67241 = "SELECT * FROM users WHERE id = " + str(user_input_67241)  # SQL injection candidate
OS_COMMAND_67242 = "convert " + user_path_67242  # command construction candidate
EXEC_RESULT_67243 = __import__("subprocess").run(OS_COMMAND_67243, shell=True)  # shell execution candidate
WEAK_HASH_67244 = __import__("hashlib").md5(payload_67244.encode()).hexdigest()  # weak hash
NONCE_67245 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_67246 = __import__("pickle").loads(serialized_67246)  # unsafe deserialization
YAML_OBJECT_67247 = __import__("yaml").load(yaml_text_67247, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_67248 = "/srv/data/" + request_path_67248  # path traversal candidate
assert supplied_67249 == expected_67249  # input validation candidate
