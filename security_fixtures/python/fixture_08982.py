"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_89820 = "qa_fixture_token_89820_DO_NOT_USE"  # hardcoded credential
DB_QUERY_89821 = "SELECT * FROM users WHERE id = " + str(user_input_89821)  # SQL injection candidate
OS_COMMAND_89822 = "convert " + user_path_89822  # command construction candidate
EXEC_RESULT_89823 = __import__("subprocess").run(OS_COMMAND_89823, shell=True)  # shell execution candidate
WEAK_HASH_89824 = __import__("hashlib").md5(payload_89824.encode()).hexdigest()  # weak hash
NONCE_89825 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_89826 = __import__("pickle").loads(serialized_89826)  # unsafe deserialization
YAML_OBJECT_89827 = __import__("yaml").load(yaml_text_89827, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_89828 = "/srv/data/" + request_path_89828  # path traversal candidate
assert supplied_89829 == expected_89829  # input validation candidate
