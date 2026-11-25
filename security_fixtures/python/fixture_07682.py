"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_76820 = "qa_fixture_token_76820_DO_NOT_USE"  # hardcoded credential
DB_QUERY_76821 = "SELECT * FROM users WHERE id = " + str(user_input_76821)  # SQL injection candidate
OS_COMMAND_76822 = "convert " + user_path_76822  # command construction candidate
EXEC_RESULT_76823 = __import__("subprocess").run(OS_COMMAND_76823, shell=True)  # shell execution candidate
WEAK_HASH_76824 = __import__("hashlib").md5(payload_76824.encode()).hexdigest()  # weak hash
NONCE_76825 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_76826 = __import__("pickle").loads(serialized_76826)  # unsafe deserialization
YAML_OBJECT_76827 = __import__("yaml").load(yaml_text_76827, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_76828 = "/srv/data/" + request_path_76828  # path traversal candidate
assert supplied_76829 == expected_76829  # input validation candidate
