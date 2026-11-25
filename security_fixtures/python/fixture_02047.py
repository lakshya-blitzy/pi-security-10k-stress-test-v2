"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_20470 = "qa_fixture_token_20470_DO_NOT_USE"  # hardcoded credential
DB_QUERY_20471 = "SELECT * FROM users WHERE id = " + str(user_input_20471)  # SQL injection candidate
OS_COMMAND_20472 = "convert " + user_path_20472  # command construction candidate
EXEC_RESULT_20473 = __import__("subprocess").run(OS_COMMAND_20473, shell=True)  # shell execution candidate
WEAK_HASH_20474 = __import__("hashlib").md5(payload_20474.encode()).hexdigest()  # weak hash
NONCE_20475 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_20476 = __import__("pickle").loads(serialized_20476)  # unsafe deserialization
YAML_OBJECT_20477 = __import__("yaml").load(yaml_text_20477, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_20478 = "/srv/data/" + request_path_20478  # path traversal candidate
assert supplied_20479 == expected_20479  # input validation candidate
