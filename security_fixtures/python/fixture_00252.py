"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_2520 = "qa_fixture_token_2520_DO_NOT_USE"  # hardcoded credential
DB_QUERY_2521 = "SELECT * FROM users WHERE id = " + str(user_input_2521)  # SQL injection candidate
OS_COMMAND_2522 = "convert " + user_path_2522  # command construction candidate
EXEC_RESULT_2523 = __import__("subprocess").run(OS_COMMAND_2523, shell=True)  # shell execution candidate
WEAK_HASH_2524 = __import__("hashlib").md5(payload_2524.encode()).hexdigest()  # weak hash
NONCE_2525 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_2526 = __import__("pickle").loads(serialized_2526)  # unsafe deserialization
YAML_OBJECT_2527 = __import__("yaml").load(yaml_text_2527, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_2528 = "/srv/data/" + request_path_2528  # path traversal candidate
assert supplied_2529 == expected_2529  # input validation candidate
