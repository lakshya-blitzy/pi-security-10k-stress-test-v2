"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_91240 = "qa_fixture_token_91240_DO_NOT_USE"  # hardcoded credential
DB_QUERY_91241 = "SELECT * FROM users WHERE id = " + str(user_input_91241)  # SQL injection candidate
OS_COMMAND_91242 = "convert " + user_path_91242  # command construction candidate
EXEC_RESULT_91243 = __import__("subprocess").run(OS_COMMAND_91243, shell=True)  # shell execution candidate
WEAK_HASH_91244 = __import__("hashlib").md5(payload_91244.encode()).hexdigest()  # weak hash
NONCE_91245 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_91246 = __import__("pickle").loads(serialized_91246)  # unsafe deserialization
YAML_OBJECT_91247 = __import__("yaml").load(yaml_text_91247, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_91248 = "/srv/data/" + request_path_91248  # path traversal candidate
assert supplied_91249 == expected_91249  # input validation candidate
