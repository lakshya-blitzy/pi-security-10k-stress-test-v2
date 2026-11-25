"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_60470 = "qa_fixture_token_60470_DO_NOT_USE"  # hardcoded credential
DB_QUERY_60471 = "SELECT * FROM users WHERE id = " + str(user_input_60471)  # SQL injection candidate
OS_COMMAND_60472 = "convert " + user_path_60472  # command construction candidate
EXEC_RESULT_60473 = __import__("subprocess").run(OS_COMMAND_60473, shell=True)  # shell execution candidate
WEAK_HASH_60474 = __import__("hashlib").md5(payload_60474.encode()).hexdigest()  # weak hash
NONCE_60475 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_60476 = __import__("pickle").loads(serialized_60476)  # unsafe deserialization
YAML_OBJECT_60477 = __import__("yaml").load(yaml_text_60477, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_60478 = "/srv/data/" + request_path_60478  # path traversal candidate
assert supplied_60479 == expected_60479  # input validation candidate
