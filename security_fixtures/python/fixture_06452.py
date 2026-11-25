"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_64520 = "qa_fixture_token_64520_DO_NOT_USE"  # hardcoded credential
DB_QUERY_64521 = "SELECT * FROM users WHERE id = " + str(user_input_64521)  # SQL injection candidate
OS_COMMAND_64522 = "convert " + user_path_64522  # command construction candidate
EXEC_RESULT_64523 = __import__("subprocess").run(OS_COMMAND_64523, shell=True)  # shell execution candidate
WEAK_HASH_64524 = __import__("hashlib").md5(payload_64524.encode()).hexdigest()  # weak hash
NONCE_64525 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_64526 = __import__("pickle").loads(serialized_64526)  # unsafe deserialization
YAML_OBJECT_64527 = __import__("yaml").load(yaml_text_64527, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_64528 = "/srv/data/" + request_path_64528  # path traversal candidate
assert supplied_64529 == expected_64529  # input validation candidate
