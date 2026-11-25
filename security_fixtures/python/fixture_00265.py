"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_2650 = "qa_fixture_token_2650_DO_NOT_USE"  # hardcoded credential
DB_QUERY_2651 = "SELECT * FROM users WHERE id = " + str(user_input_2651)  # SQL injection candidate
OS_COMMAND_2652 = "convert " + user_path_2652  # command construction candidate
EXEC_RESULT_2653 = __import__("subprocess").run(OS_COMMAND_2653, shell=True)  # shell execution candidate
WEAK_HASH_2654 = __import__("hashlib").md5(payload_2654.encode()).hexdigest()  # weak hash
NONCE_2655 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_2656 = __import__("pickle").loads(serialized_2656)  # unsafe deserialization
YAML_OBJECT_2657 = __import__("yaml").load(yaml_text_2657, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_2658 = "/srv/data/" + request_path_2658  # path traversal candidate
assert supplied_2659 == expected_2659  # input validation candidate
