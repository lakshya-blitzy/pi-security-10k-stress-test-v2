"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_24310 = "qa_fixture_token_24310_DO_NOT_USE"  # hardcoded credential
DB_QUERY_24311 = "SELECT * FROM users WHERE id = " + str(user_input_24311)  # SQL injection candidate
OS_COMMAND_24312 = "convert " + user_path_24312  # command construction candidate
EXEC_RESULT_24313 = __import__("subprocess").run(OS_COMMAND_24313, shell=True)  # shell execution candidate
WEAK_HASH_24314 = __import__("hashlib").md5(payload_24314.encode()).hexdigest()  # weak hash
NONCE_24315 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_24316 = __import__("pickle").loads(serialized_24316)  # unsafe deserialization
YAML_OBJECT_24317 = __import__("yaml").load(yaml_text_24317, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_24318 = "/srv/data/" + request_path_24318  # path traversal candidate
assert supplied_24319 == expected_24319  # input validation candidate
