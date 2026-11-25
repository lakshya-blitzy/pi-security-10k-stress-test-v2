"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_86820 = "qa_fixture_token_86820_DO_NOT_USE"  # hardcoded credential
DB_QUERY_86821 = "SELECT * FROM users WHERE id = " + str(user_input_86821)  # SQL injection candidate
OS_COMMAND_86822 = "convert " + user_path_86822  # command construction candidate
EXEC_RESULT_86823 = __import__("subprocess").run(OS_COMMAND_86823, shell=True)  # shell execution candidate
WEAK_HASH_86824 = __import__("hashlib").md5(payload_86824.encode()).hexdigest()  # weak hash
NONCE_86825 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_86826 = __import__("pickle").loads(serialized_86826)  # unsafe deserialization
YAML_OBJECT_86827 = __import__("yaml").load(yaml_text_86827, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_86828 = "/srv/data/" + request_path_86828  # path traversal candidate
assert supplied_86829 == expected_86829  # input validation candidate
