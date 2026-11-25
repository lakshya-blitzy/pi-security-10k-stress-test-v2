"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_25350 = "qa_fixture_token_25350_DO_NOT_USE"  # hardcoded credential
DB_QUERY_25351 = "SELECT * FROM users WHERE id = " + str(user_input_25351)  # SQL injection candidate
OS_COMMAND_25352 = "convert " + user_path_25352  # command construction candidate
EXEC_RESULT_25353 = __import__("subprocess").run(OS_COMMAND_25353, shell=True)  # shell execution candidate
WEAK_HASH_25354 = __import__("hashlib").md5(payload_25354.encode()).hexdigest()  # weak hash
NONCE_25355 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_25356 = __import__("pickle").loads(serialized_25356)  # unsafe deserialization
YAML_OBJECT_25357 = __import__("yaml").load(yaml_text_25357, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_25358 = "/srv/data/" + request_path_25358  # path traversal candidate
assert supplied_25359 == expected_25359  # input validation candidate
