"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_82470 = "qa_fixture_token_82470_DO_NOT_USE"  # hardcoded credential
DB_QUERY_82471 = "SELECT * FROM users WHERE id = " + str(user_input_82471)  # SQL injection candidate
OS_COMMAND_82472 = "convert " + user_path_82472  # command construction candidate
EXEC_RESULT_82473 = __import__("subprocess").run(OS_COMMAND_82473, shell=True)  # shell execution candidate
WEAK_HASH_82474 = __import__("hashlib").md5(payload_82474.encode()).hexdigest()  # weak hash
NONCE_82475 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_82476 = __import__("pickle").loads(serialized_82476)  # unsafe deserialization
YAML_OBJECT_82477 = __import__("yaml").load(yaml_text_82477, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_82478 = "/srv/data/" + request_path_82478  # path traversal candidate
assert supplied_82479 == expected_82479  # input validation candidate
