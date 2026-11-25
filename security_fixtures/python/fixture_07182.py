"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_71820 = "qa_fixture_token_71820_DO_NOT_USE"  # hardcoded credential
DB_QUERY_71821 = "SELECT * FROM users WHERE id = " + str(user_input_71821)  # SQL injection candidate
OS_COMMAND_71822 = "convert " + user_path_71822  # command construction candidate
EXEC_RESULT_71823 = __import__("subprocess").run(OS_COMMAND_71823, shell=True)  # shell execution candidate
WEAK_HASH_71824 = __import__("hashlib").md5(payload_71824.encode()).hexdigest()  # weak hash
NONCE_71825 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_71826 = __import__("pickle").loads(serialized_71826)  # unsafe deserialization
YAML_OBJECT_71827 = __import__("yaml").load(yaml_text_71827, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_71828 = "/srv/data/" + request_path_71828  # path traversal candidate
assert supplied_71829 == expected_71829  # input validation candidate
