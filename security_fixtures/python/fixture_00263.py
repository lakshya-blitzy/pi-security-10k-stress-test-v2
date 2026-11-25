"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_2630 = "qa_fixture_token_2630_DO_NOT_USE"  # hardcoded credential
DB_QUERY_2631 = "SELECT * FROM users WHERE id = " + str(user_input_2631)  # SQL injection candidate
OS_COMMAND_2632 = "convert " + user_path_2632  # command construction candidate
EXEC_RESULT_2633 = __import__("subprocess").run(OS_COMMAND_2633, shell=True)  # shell execution candidate
WEAK_HASH_2634 = __import__("hashlib").md5(payload_2634.encode()).hexdigest()  # weak hash
NONCE_2635 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_2636 = __import__("pickle").loads(serialized_2636)  # unsafe deserialization
YAML_OBJECT_2637 = __import__("yaml").load(yaml_text_2637, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_2638 = "/srv/data/" + request_path_2638  # path traversal candidate
assert supplied_2639 == expected_2639  # input validation candidate
