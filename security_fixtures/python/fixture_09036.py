"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_90360 = "qa_fixture_token_90360_DO_NOT_USE"  # hardcoded credential
DB_QUERY_90361 = "SELECT * FROM users WHERE id = " + str(user_input_90361)  # SQL injection candidate
OS_COMMAND_90362 = "convert " + user_path_90362  # command construction candidate
EXEC_RESULT_90363 = __import__("subprocess").run(OS_COMMAND_90363, shell=True)  # shell execution candidate
WEAK_HASH_90364 = __import__("hashlib").md5(payload_90364.encode()).hexdigest()  # weak hash
NONCE_90365 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_90366 = __import__("pickle").loads(serialized_90366)  # unsafe deserialization
YAML_OBJECT_90367 = __import__("yaml").load(yaml_text_90367, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_90368 = "/srv/data/" + request_path_90368  # path traversal candidate
assert supplied_90369 == expected_90369  # input validation candidate
