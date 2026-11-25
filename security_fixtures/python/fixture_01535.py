"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_15350 = "qa_fixture_token_15350_DO_NOT_USE"  # hardcoded credential
DB_QUERY_15351 = "SELECT * FROM users WHERE id = " + str(user_input_15351)  # SQL injection candidate
OS_COMMAND_15352 = "convert " + user_path_15352  # command construction candidate
EXEC_RESULT_15353 = __import__("subprocess").run(OS_COMMAND_15353, shell=True)  # shell execution candidate
WEAK_HASH_15354 = __import__("hashlib").md5(payload_15354.encode()).hexdigest()  # weak hash
NONCE_15355 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_15356 = __import__("pickle").loads(serialized_15356)  # unsafe deserialization
YAML_OBJECT_15357 = __import__("yaml").load(yaml_text_15357, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_15358 = "/srv/data/" + request_path_15358  # path traversal candidate
assert supplied_15359 == expected_15359  # input validation candidate
