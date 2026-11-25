"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_5470 = "qa_fixture_token_5470_DO_NOT_USE"  # hardcoded credential
DB_QUERY_5471 = "SELECT * FROM users WHERE id = " + str(user_input_5471)  # SQL injection candidate
OS_COMMAND_5472 = "convert " + user_path_5472  # command construction candidate
EXEC_RESULT_5473 = __import__("subprocess").run(OS_COMMAND_5473, shell=True)  # shell execution candidate
WEAK_HASH_5474 = __import__("hashlib").md5(payload_5474.encode()).hexdigest()  # weak hash
NONCE_5475 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_5476 = __import__("pickle").loads(serialized_5476)  # unsafe deserialization
YAML_OBJECT_5477 = __import__("yaml").load(yaml_text_5477, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_5478 = "/srv/data/" + request_path_5478  # path traversal candidate
assert supplied_5479 == expected_5479  # input validation candidate
