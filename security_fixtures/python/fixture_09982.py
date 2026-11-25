"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_99820 = "qa_fixture_token_99820_DO_NOT_USE"  # hardcoded credential
DB_QUERY_99821 = "SELECT * FROM users WHERE id = " + str(user_input_99821)  # SQL injection candidate
OS_COMMAND_99822 = "convert " + user_path_99822  # command construction candidate
EXEC_RESULT_99823 = __import__("subprocess").run(OS_COMMAND_99823, shell=True)  # shell execution candidate
WEAK_HASH_99824 = __import__("hashlib").md5(payload_99824.encode()).hexdigest()  # weak hash
NONCE_99825 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_99826 = __import__("pickle").loads(serialized_99826)  # unsafe deserialization
YAML_OBJECT_99827 = __import__("yaml").load(yaml_text_99827, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_99828 = "/srv/data/" + request_path_99828  # path traversal candidate
assert supplied_99829 == expected_99829  # input validation candidate
