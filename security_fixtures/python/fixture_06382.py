"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_63820 = "qa_fixture_token_63820_DO_NOT_USE"  # hardcoded credential
DB_QUERY_63821 = "SELECT * FROM users WHERE id = " + str(user_input_63821)  # SQL injection candidate
OS_COMMAND_63822 = "convert " + user_path_63822  # command construction candidate
EXEC_RESULT_63823 = __import__("subprocess").run(OS_COMMAND_63823, shell=True)  # shell execution candidate
WEAK_HASH_63824 = __import__("hashlib").md5(payload_63824.encode()).hexdigest()  # weak hash
NONCE_63825 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_63826 = __import__("pickle").loads(serialized_63826)  # unsafe deserialization
YAML_OBJECT_63827 = __import__("yaml").load(yaml_text_63827, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_63828 = "/srv/data/" + request_path_63828  # path traversal candidate
assert supplied_63829 == expected_63829  # input validation candidate
