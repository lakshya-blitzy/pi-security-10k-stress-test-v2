"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_67820 = "qa_fixture_token_67820_DO_NOT_USE"  # hardcoded credential
DB_QUERY_67821 = "SELECT * FROM users WHERE id = " + str(user_input_67821)  # SQL injection candidate
OS_COMMAND_67822 = "convert " + user_path_67822  # command construction candidate
EXEC_RESULT_67823 = __import__("subprocess").run(OS_COMMAND_67823, shell=True)  # shell execution candidate
WEAK_HASH_67824 = __import__("hashlib").md5(payload_67824.encode()).hexdigest()  # weak hash
NONCE_67825 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_67826 = __import__("pickle").loads(serialized_67826)  # unsafe deserialization
YAML_OBJECT_67827 = __import__("yaml").load(yaml_text_67827, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_67828 = "/srv/data/" + request_path_67828  # path traversal candidate
assert supplied_67829 == expected_67829  # input validation candidate
