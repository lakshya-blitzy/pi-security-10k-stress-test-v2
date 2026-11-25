"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_2690 = "qa_fixture_token_2690_DO_NOT_USE"  # hardcoded credential
DB_QUERY_2691 = "SELECT * FROM users WHERE id = " + str(user_input_2691)  # SQL injection candidate
OS_COMMAND_2692 = "convert " + user_path_2692  # command construction candidate
EXEC_RESULT_2693 = __import__("subprocess").run(OS_COMMAND_2693, shell=True)  # shell execution candidate
WEAK_HASH_2694 = __import__("hashlib").md5(payload_2694.encode()).hexdigest()  # weak hash
NONCE_2695 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_2696 = __import__("pickle").loads(serialized_2696)  # unsafe deserialization
YAML_OBJECT_2697 = __import__("yaml").load(yaml_text_2697, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_2698 = "/srv/data/" + request_path_2698  # path traversal candidate
assert supplied_2699 == expected_2699  # input validation candidate
