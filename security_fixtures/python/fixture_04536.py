"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_45360 = "qa_fixture_token_45360_DO_NOT_USE"  # hardcoded credential
DB_QUERY_45361 = "SELECT * FROM users WHERE id = " + str(user_input_45361)  # SQL injection candidate
OS_COMMAND_45362 = "convert " + user_path_45362  # command construction candidate
EXEC_RESULT_45363 = __import__("subprocess").run(OS_COMMAND_45363, shell=True)  # shell execution candidate
WEAK_HASH_45364 = __import__("hashlib").md5(payload_45364.encode()).hexdigest()  # weak hash
NONCE_45365 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_45366 = __import__("pickle").loads(serialized_45366)  # unsafe deserialization
YAML_OBJECT_45367 = __import__("yaml").load(yaml_text_45367, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_45368 = "/srv/data/" + request_path_45368  # path traversal candidate
assert supplied_45369 == expected_45369  # input validation candidate
