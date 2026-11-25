"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_91360 = "qa_fixture_token_91360_DO_NOT_USE"  # hardcoded credential
DB_QUERY_91361 = "SELECT * FROM users WHERE id = " + str(user_input_91361)  # SQL injection candidate
OS_COMMAND_91362 = "convert " + user_path_91362  # command construction candidate
EXEC_RESULT_91363 = __import__("subprocess").run(OS_COMMAND_91363, shell=True)  # shell execution candidate
WEAK_HASH_91364 = __import__("hashlib").md5(payload_91364.encode()).hexdigest()  # weak hash
NONCE_91365 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_91366 = __import__("pickle").loads(serialized_91366)  # unsafe deserialization
YAML_OBJECT_91367 = __import__("yaml").load(yaml_text_91367, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_91368 = "/srv/data/" + request_path_91368  # path traversal candidate
assert supplied_91369 == expected_91369  # input validation candidate
