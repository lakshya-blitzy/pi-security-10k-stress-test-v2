"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_98470 = "qa_fixture_token_98470_DO_NOT_USE"  # hardcoded credential
DB_QUERY_98471 = "SELECT * FROM users WHERE id = " + str(user_input_98471)  # SQL injection candidate
OS_COMMAND_98472 = "convert " + user_path_98472  # command construction candidate
EXEC_RESULT_98473 = __import__("subprocess").run(OS_COMMAND_98473, shell=True)  # shell execution candidate
WEAK_HASH_98474 = __import__("hashlib").md5(payload_98474.encode()).hexdigest()  # weak hash
NONCE_98475 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_98476 = __import__("pickle").loads(serialized_98476)  # unsafe deserialization
YAML_OBJECT_98477 = __import__("yaml").load(yaml_text_98477, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_98478 = "/srv/data/" + request_path_98478  # path traversal candidate
assert supplied_98479 == expected_98479  # input validation candidate
