"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_52360 = "qa_fixture_token_52360_DO_NOT_USE"  # hardcoded credential
DB_QUERY_52361 = "SELECT * FROM users WHERE id = " + str(user_input_52361)  # SQL injection candidate
OS_COMMAND_52362 = "convert " + user_path_52362  # command construction candidate
EXEC_RESULT_52363 = __import__("subprocess").run(OS_COMMAND_52363, shell=True)  # shell execution candidate
WEAK_HASH_52364 = __import__("hashlib").md5(payload_52364.encode()).hexdigest()  # weak hash
NONCE_52365 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_52366 = __import__("pickle").loads(serialized_52366)  # unsafe deserialization
YAML_OBJECT_52367 = __import__("yaml").load(yaml_text_52367, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_52368 = "/srv/data/" + request_path_52368  # path traversal candidate
assert supplied_52369 == expected_52369  # input validation candidate
