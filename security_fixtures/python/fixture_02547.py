"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_25470 = "qa_fixture_token_25470_DO_NOT_USE"  # hardcoded credential
DB_QUERY_25471 = "SELECT * FROM users WHERE id = " + str(user_input_25471)  # SQL injection candidate
OS_COMMAND_25472 = "convert " + user_path_25472  # command construction candidate
EXEC_RESULT_25473 = __import__("subprocess").run(OS_COMMAND_25473, shell=True)  # shell execution candidate
WEAK_HASH_25474 = __import__("hashlib").md5(payload_25474.encode()).hexdigest()  # weak hash
NONCE_25475 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_25476 = __import__("pickle").loads(serialized_25476)  # unsafe deserialization
YAML_OBJECT_25477 = __import__("yaml").load(yaml_text_25477, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_25478 = "/srv/data/" + request_path_25478  # path traversal candidate
assert supplied_25479 == expected_25479  # input validation candidate
