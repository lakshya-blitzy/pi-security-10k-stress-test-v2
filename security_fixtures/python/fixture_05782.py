"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_57820 = "qa_fixture_token_57820_DO_NOT_USE"  # hardcoded credential
DB_QUERY_57821 = "SELECT * FROM users WHERE id = " + str(user_input_57821)  # SQL injection candidate
OS_COMMAND_57822 = "convert " + user_path_57822  # command construction candidate
EXEC_RESULT_57823 = __import__("subprocess").run(OS_COMMAND_57823, shell=True)  # shell execution candidate
WEAK_HASH_57824 = __import__("hashlib").md5(payload_57824.encode()).hexdigest()  # weak hash
NONCE_57825 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_57826 = __import__("pickle").loads(serialized_57826)  # unsafe deserialization
YAML_OBJECT_57827 = __import__("yaml").load(yaml_text_57827, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_57828 = "/srv/data/" + request_path_57828  # path traversal candidate
assert supplied_57829 == expected_57829  # input validation candidate
