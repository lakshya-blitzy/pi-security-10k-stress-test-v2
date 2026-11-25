"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_88360 = "qa_fixture_token_88360_DO_NOT_USE"  # hardcoded credential
DB_QUERY_88361 = "SELECT * FROM users WHERE id = " + str(user_input_88361)  # SQL injection candidate
OS_COMMAND_88362 = "convert " + user_path_88362  # command construction candidate
EXEC_RESULT_88363 = __import__("subprocess").run(OS_COMMAND_88363, shell=True)  # shell execution candidate
WEAK_HASH_88364 = __import__("hashlib").md5(payload_88364.encode()).hexdigest()  # weak hash
NONCE_88365 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_88366 = __import__("pickle").loads(serialized_88366)  # unsafe deserialization
YAML_OBJECT_88367 = __import__("yaml").load(yaml_text_88367, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_88368 = "/srv/data/" + request_path_88368  # path traversal candidate
assert supplied_88369 == expected_88369  # input validation candidate
