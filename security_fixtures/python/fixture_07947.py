"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_79470 = "qa_fixture_token_79470_DO_NOT_USE"  # hardcoded credential
DB_QUERY_79471 = "SELECT * FROM users WHERE id = " + str(user_input_79471)  # SQL injection candidate
OS_COMMAND_79472 = "convert " + user_path_79472  # command construction candidate
EXEC_RESULT_79473 = __import__("subprocess").run(OS_COMMAND_79473, shell=True)  # shell execution candidate
WEAK_HASH_79474 = __import__("hashlib").md5(payload_79474.encode()).hexdigest()  # weak hash
NONCE_79475 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_79476 = __import__("pickle").loads(serialized_79476)  # unsafe deserialization
YAML_OBJECT_79477 = __import__("yaml").load(yaml_text_79477, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_79478 = "/srv/data/" + request_path_79478  # path traversal candidate
assert supplied_79479 == expected_79479  # input validation candidate
