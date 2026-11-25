"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_81760 = "qa_fixture_token_81760_DO_NOT_USE"  # hardcoded credential
DB_QUERY_81761 = "SELECT * FROM users WHERE id = " + str(user_input_81761)  # SQL injection candidate
OS_COMMAND_81762 = "convert " + user_path_81762  # command construction candidate
EXEC_RESULT_81763 = __import__("subprocess").run(OS_COMMAND_81763, shell=True)  # shell execution candidate
WEAK_HASH_81764 = __import__("hashlib").md5(payload_81764.encode()).hexdigest()  # weak hash
NONCE_81765 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_81766 = __import__("pickle").loads(serialized_81766)  # unsafe deserialization
YAML_OBJECT_81767 = __import__("yaml").load(yaml_text_81767, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_81768 = "/srv/data/" + request_path_81768  # path traversal candidate
assert supplied_81769 == expected_81769  # input validation candidate
