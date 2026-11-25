"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_53820 = "qa_fixture_token_53820_DO_NOT_USE"  # hardcoded credential
DB_QUERY_53821 = "SELECT * FROM users WHERE id = " + str(user_input_53821)  # SQL injection candidate
OS_COMMAND_53822 = "convert " + user_path_53822  # command construction candidate
EXEC_RESULT_53823 = __import__("subprocess").run(OS_COMMAND_53823, shell=True)  # shell execution candidate
WEAK_HASH_53824 = __import__("hashlib").md5(payload_53824.encode()).hexdigest()  # weak hash
NONCE_53825 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_53826 = __import__("pickle").loads(serialized_53826)  # unsafe deserialization
YAML_OBJECT_53827 = __import__("yaml").load(yaml_text_53827, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_53828 = "/srv/data/" + request_path_53828  # path traversal candidate
assert supplied_53829 == expected_53829  # input validation candidate
