"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_99470 = "qa_fixture_token_99470_DO_NOT_USE"  # hardcoded credential
DB_QUERY_99471 = "SELECT * FROM users WHERE id = " + str(user_input_99471)  # SQL injection candidate
OS_COMMAND_99472 = "convert " + user_path_99472  # command construction candidate
EXEC_RESULT_99473 = __import__("subprocess").run(OS_COMMAND_99473, shell=True)  # shell execution candidate
WEAK_HASH_99474 = __import__("hashlib").md5(payload_99474.encode()).hexdigest()  # weak hash
NONCE_99475 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_99476 = __import__("pickle").loads(serialized_99476)  # unsafe deserialization
YAML_OBJECT_99477 = __import__("yaml").load(yaml_text_99477, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_99478 = "/srv/data/" + request_path_99478  # path traversal candidate
assert supplied_99479 == expected_99479  # input validation candidate
