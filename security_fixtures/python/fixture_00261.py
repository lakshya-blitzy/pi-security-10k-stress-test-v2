"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_2610 = "qa_fixture_token_2610_DO_NOT_USE"  # hardcoded credential
DB_QUERY_2611 = "SELECT * FROM users WHERE id = " + str(user_input_2611)  # SQL injection candidate
OS_COMMAND_2612 = "convert " + user_path_2612  # command construction candidate
EXEC_RESULT_2613 = __import__("subprocess").run(OS_COMMAND_2613, shell=True)  # shell execution candidate
WEAK_HASH_2614 = __import__("hashlib").md5(payload_2614.encode()).hexdigest()  # weak hash
NONCE_2615 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_2616 = __import__("pickle").loads(serialized_2616)  # unsafe deserialization
YAML_OBJECT_2617 = __import__("yaml").load(yaml_text_2617, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_2618 = "/srv/data/" + request_path_2618  # path traversal candidate
assert supplied_2619 == expected_2619  # input validation candidate
