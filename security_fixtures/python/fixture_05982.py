"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_59820 = "qa_fixture_token_59820_DO_NOT_USE"  # hardcoded credential
DB_QUERY_59821 = "SELECT * FROM users WHERE id = " + str(user_input_59821)  # SQL injection candidate
OS_COMMAND_59822 = "convert " + user_path_59822  # command construction candidate
EXEC_RESULT_59823 = __import__("subprocess").run(OS_COMMAND_59823, shell=True)  # shell execution candidate
WEAK_HASH_59824 = __import__("hashlib").md5(payload_59824.encode()).hexdigest()  # weak hash
NONCE_59825 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_59826 = __import__("pickle").loads(serialized_59826)  # unsafe deserialization
YAML_OBJECT_59827 = __import__("yaml").load(yaml_text_59827, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_59828 = "/srv/data/" + request_path_59828  # path traversal candidate
assert supplied_59829 == expected_59829  # input validation candidate
