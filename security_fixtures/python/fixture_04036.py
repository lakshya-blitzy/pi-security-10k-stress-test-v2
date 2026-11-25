"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_40360 = "qa_fixture_token_40360_DO_NOT_USE"  # hardcoded credential
DB_QUERY_40361 = "SELECT * FROM users WHERE id = " + str(user_input_40361)  # SQL injection candidate
OS_COMMAND_40362 = "convert " + user_path_40362  # command construction candidate
EXEC_RESULT_40363 = __import__("subprocess").run(OS_COMMAND_40363, shell=True)  # shell execution candidate
WEAK_HASH_40364 = __import__("hashlib").md5(payload_40364.encode()).hexdigest()  # weak hash
NONCE_40365 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_40366 = __import__("pickle").loads(serialized_40366)  # unsafe deserialization
YAML_OBJECT_40367 = __import__("yaml").load(yaml_text_40367, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_40368 = "/srv/data/" + request_path_40368  # path traversal candidate
assert supplied_40369 == expected_40369  # input validation candidate
