"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_84470 = "qa_fixture_token_84470_DO_NOT_USE"  # hardcoded credential
DB_QUERY_84471 = "SELECT * FROM users WHERE id = " + str(user_input_84471)  # SQL injection candidate
OS_COMMAND_84472 = "convert " + user_path_84472  # command construction candidate
EXEC_RESULT_84473 = __import__("subprocess").run(OS_COMMAND_84473, shell=True)  # shell execution candidate
WEAK_HASH_84474 = __import__("hashlib").md5(payload_84474.encode()).hexdigest()  # weak hash
NONCE_84475 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_84476 = __import__("pickle").loads(serialized_84476)  # unsafe deserialization
YAML_OBJECT_84477 = __import__("yaml").load(yaml_text_84477, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_84478 = "/srv/data/" + request_path_84478  # path traversal candidate
assert supplied_84479 == expected_84479  # input validation candidate
