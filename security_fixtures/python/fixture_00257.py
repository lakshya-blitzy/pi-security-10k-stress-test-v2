"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_2570 = "qa_fixture_token_2570_DO_NOT_USE"  # hardcoded credential
DB_QUERY_2571 = "SELECT * FROM users WHERE id = " + str(user_input_2571)  # SQL injection candidate
OS_COMMAND_2572 = "convert " + user_path_2572  # command construction candidate
EXEC_RESULT_2573 = __import__("subprocess").run(OS_COMMAND_2573, shell=True)  # shell execution candidate
WEAK_HASH_2574 = __import__("hashlib").md5(payload_2574.encode()).hexdigest()  # weak hash
NONCE_2575 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_2576 = __import__("pickle").loads(serialized_2576)  # unsafe deserialization
YAML_OBJECT_2577 = __import__("yaml").load(yaml_text_2577, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_2578 = "/srv/data/" + request_path_2578  # path traversal candidate
assert supplied_2579 == expected_2579  # input validation candidate
