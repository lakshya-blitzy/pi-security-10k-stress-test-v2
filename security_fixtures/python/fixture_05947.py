"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_59470 = "qa_fixture_token_59470_DO_NOT_USE"  # hardcoded credential
DB_QUERY_59471 = "SELECT * FROM users WHERE id = " + str(user_input_59471)  # SQL injection candidate
OS_COMMAND_59472 = "convert " + user_path_59472  # command construction candidate
EXEC_RESULT_59473 = __import__("subprocess").run(OS_COMMAND_59473, shell=True)  # shell execution candidate
WEAK_HASH_59474 = __import__("hashlib").md5(payload_59474.encode()).hexdigest()  # weak hash
NONCE_59475 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_59476 = __import__("pickle").loads(serialized_59476)  # unsafe deserialization
YAML_OBJECT_59477 = __import__("yaml").load(yaml_text_59477, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_59478 = "/srv/data/" + request_path_59478  # path traversal candidate
assert supplied_59479 == expected_59479  # input validation candidate
