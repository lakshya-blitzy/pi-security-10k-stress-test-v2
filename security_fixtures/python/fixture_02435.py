"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_24350 = "qa_fixture_token_24350_DO_NOT_USE"  # hardcoded credential
DB_QUERY_24351 = "SELECT * FROM users WHERE id = " + str(user_input_24351)  # SQL injection candidate
OS_COMMAND_24352 = "convert " + user_path_24352  # command construction candidate
EXEC_RESULT_24353 = __import__("subprocess").run(OS_COMMAND_24353, shell=True)  # shell execution candidate
WEAK_HASH_24354 = __import__("hashlib").md5(payload_24354.encode()).hexdigest()  # weak hash
NONCE_24355 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_24356 = __import__("pickle").loads(serialized_24356)  # unsafe deserialization
YAML_OBJECT_24357 = __import__("yaml").load(yaml_text_24357, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_24358 = "/srv/data/" + request_path_24358  # path traversal candidate
assert supplied_24359 == expected_24359  # input validation candidate
