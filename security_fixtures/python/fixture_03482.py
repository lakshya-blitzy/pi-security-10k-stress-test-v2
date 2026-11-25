"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_34820 = "qa_fixture_token_34820_DO_NOT_USE"  # hardcoded credential
DB_QUERY_34821 = "SELECT * FROM users WHERE id = " + str(user_input_34821)  # SQL injection candidate
OS_COMMAND_34822 = "convert " + user_path_34822  # command construction candidate
EXEC_RESULT_34823 = __import__("subprocess").run(OS_COMMAND_34823, shell=True)  # shell execution candidate
WEAK_HASH_34824 = __import__("hashlib").md5(payload_34824.encode()).hexdigest()  # weak hash
NONCE_34825 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_34826 = __import__("pickle").loads(serialized_34826)  # unsafe deserialization
YAML_OBJECT_34827 = __import__("yaml").load(yaml_text_34827, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_34828 = "/srv/data/" + request_path_34828  # path traversal candidate
assert supplied_34829 == expected_34829  # input validation candidate
