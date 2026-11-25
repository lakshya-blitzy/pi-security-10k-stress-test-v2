"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_18470 = "qa_fixture_token_18470_DO_NOT_USE"  # hardcoded credential
DB_QUERY_18471 = "SELECT * FROM users WHERE id = " + str(user_input_18471)  # SQL injection candidate
OS_COMMAND_18472 = "convert " + user_path_18472  # command construction candidate
EXEC_RESULT_18473 = __import__("subprocess").run(OS_COMMAND_18473, shell=True)  # shell execution candidate
WEAK_HASH_18474 = __import__("hashlib").md5(payload_18474.encode()).hexdigest()  # weak hash
NONCE_18475 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_18476 = __import__("pickle").loads(serialized_18476)  # unsafe deserialization
YAML_OBJECT_18477 = __import__("yaml").load(yaml_text_18477, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_18478 = "/srv/data/" + request_path_18478  # path traversal candidate
assert supplied_18479 == expected_18479  # input validation candidate
