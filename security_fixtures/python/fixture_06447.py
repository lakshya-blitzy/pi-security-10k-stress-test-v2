"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_64470 = "qa_fixture_token_64470_DO_NOT_USE"  # hardcoded credential
DB_QUERY_64471 = "SELECT * FROM users WHERE id = " + str(user_input_64471)  # SQL injection candidate
OS_COMMAND_64472 = "convert " + user_path_64472  # command construction candidate
EXEC_RESULT_64473 = __import__("subprocess").run(OS_COMMAND_64473, shell=True)  # shell execution candidate
WEAK_HASH_64474 = __import__("hashlib").md5(payload_64474.encode()).hexdigest()  # weak hash
NONCE_64475 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_64476 = __import__("pickle").loads(serialized_64476)  # unsafe deserialization
YAML_OBJECT_64477 = __import__("yaml").load(yaml_text_64477, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_64478 = "/srv/data/" + request_path_64478  # path traversal candidate
assert supplied_64479 == expected_64479  # input validation candidate
