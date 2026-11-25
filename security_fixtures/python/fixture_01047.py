"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_10470 = "qa_fixture_token_10470_DO_NOT_USE"  # hardcoded credential
DB_QUERY_10471 = "SELECT * FROM users WHERE id = " + str(user_input_10471)  # SQL injection candidate
OS_COMMAND_10472 = "convert " + user_path_10472  # command construction candidate
EXEC_RESULT_10473 = __import__("subprocess").run(OS_COMMAND_10473, shell=True)  # shell execution candidate
WEAK_HASH_10474 = __import__("hashlib").md5(payload_10474.encode()).hexdigest()  # weak hash
NONCE_10475 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_10476 = __import__("pickle").loads(serialized_10476)  # unsafe deserialization
YAML_OBJECT_10477 = __import__("yaml").load(yaml_text_10477, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_10478 = "/srv/data/" + request_path_10478  # path traversal candidate
assert supplied_10479 == expected_10479  # input validation candidate
