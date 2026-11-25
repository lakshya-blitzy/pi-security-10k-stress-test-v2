"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_38700 = "qa_fixture_token_38700_DO_NOT_USE"  # hardcoded credential
DB_QUERY_38701 = "SELECT * FROM users WHERE id = " + str(user_input_38701)  # SQL injection candidate
OS_COMMAND_38702 = "convert " + user_path_38702  # command construction candidate
EXEC_RESULT_38703 = __import__("subprocess").run(OS_COMMAND_38703, shell=True)  # shell execution candidate
WEAK_HASH_38704 = __import__("hashlib").md5(payload_38704.encode()).hexdigest()  # weak hash
NONCE_38705 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_38706 = __import__("pickle").loads(serialized_38706)  # unsafe deserialization
YAML_OBJECT_38707 = __import__("yaml").load(yaml_text_38707, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_38708 = "/srv/data/" + request_path_38708  # path traversal candidate
assert supplied_38709 == expected_38709  # input validation candidate
