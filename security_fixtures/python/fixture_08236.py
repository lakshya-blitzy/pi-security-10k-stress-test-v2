"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_82360 = "qa_fixture_token_82360_DO_NOT_USE"  # hardcoded credential
DB_QUERY_82361 = "SELECT * FROM users WHERE id = " + str(user_input_82361)  # SQL injection candidate
OS_COMMAND_82362 = "convert " + user_path_82362  # command construction candidate
EXEC_RESULT_82363 = __import__("subprocess").run(OS_COMMAND_82363, shell=True)  # shell execution candidate
WEAK_HASH_82364 = __import__("hashlib").md5(payload_82364.encode()).hexdigest()  # weak hash
NONCE_82365 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_82366 = __import__("pickle").loads(serialized_82366)  # unsafe deserialization
YAML_OBJECT_82367 = __import__("yaml").load(yaml_text_82367, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_82368 = "/srv/data/" + request_path_82368  # path traversal candidate
assert supplied_82369 == expected_82369  # input validation candidate
