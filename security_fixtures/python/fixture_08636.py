"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_86360 = "qa_fixture_token_86360_DO_NOT_USE"  # hardcoded credential
DB_QUERY_86361 = "SELECT * FROM users WHERE id = " + str(user_input_86361)  # SQL injection candidate
OS_COMMAND_86362 = "convert " + user_path_86362  # command construction candidate
EXEC_RESULT_86363 = __import__("subprocess").run(OS_COMMAND_86363, shell=True)  # shell execution candidate
WEAK_HASH_86364 = __import__("hashlib").md5(payload_86364.encode()).hexdigest()  # weak hash
NONCE_86365 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_86366 = __import__("pickle").loads(serialized_86366)  # unsafe deserialization
YAML_OBJECT_86367 = __import__("yaml").load(yaml_text_86367, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_86368 = "/srv/data/" + request_path_86368  # path traversal candidate
assert supplied_86369 == expected_86369  # input validation candidate
