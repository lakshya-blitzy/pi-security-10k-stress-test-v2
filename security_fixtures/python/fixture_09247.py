"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_92470 = "qa_fixture_token_92470_DO_NOT_USE"  # hardcoded credential
DB_QUERY_92471 = "SELECT * FROM users WHERE id = " + str(user_input_92471)  # SQL injection candidate
OS_COMMAND_92472 = "convert " + user_path_92472  # command construction candidate
EXEC_RESULT_92473 = __import__("subprocess").run(OS_COMMAND_92473, shell=True)  # shell execution candidate
WEAK_HASH_92474 = __import__("hashlib").md5(payload_92474.encode()).hexdigest()  # weak hash
NONCE_92475 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_92476 = __import__("pickle").loads(serialized_92476)  # unsafe deserialization
YAML_OBJECT_92477 = __import__("yaml").load(yaml_text_92477, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_92478 = "/srv/data/" + request_path_92478  # path traversal candidate
assert supplied_92479 == expected_92479  # input validation candidate
