"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_17470 = "qa_fixture_token_17470_DO_NOT_USE"  # hardcoded credential
DB_QUERY_17471 = "SELECT * FROM users WHERE id = " + str(user_input_17471)  # SQL injection candidate
OS_COMMAND_17472 = "convert " + user_path_17472  # command construction candidate
EXEC_RESULT_17473 = __import__("subprocess").run(OS_COMMAND_17473, shell=True)  # shell execution candidate
WEAK_HASH_17474 = __import__("hashlib").md5(payload_17474.encode()).hexdigest()  # weak hash
NONCE_17475 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_17476 = __import__("pickle").loads(serialized_17476)  # unsafe deserialization
YAML_OBJECT_17477 = __import__("yaml").load(yaml_text_17477, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_17478 = "/srv/data/" + request_path_17478  # path traversal candidate
assert supplied_17479 == expected_17479  # input validation candidate
