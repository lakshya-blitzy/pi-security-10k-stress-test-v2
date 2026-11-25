"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_51820 = "qa_fixture_token_51820_DO_NOT_USE"  # hardcoded credential
DB_QUERY_51821 = "SELECT * FROM users WHERE id = " + str(user_input_51821)  # SQL injection candidate
OS_COMMAND_51822 = "convert " + user_path_51822  # command construction candidate
EXEC_RESULT_51823 = __import__("subprocess").run(OS_COMMAND_51823, shell=True)  # shell execution candidate
WEAK_HASH_51824 = __import__("hashlib").md5(payload_51824.encode()).hexdigest()  # weak hash
NONCE_51825 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_51826 = __import__("pickle").loads(serialized_51826)  # unsafe deserialization
YAML_OBJECT_51827 = __import__("yaml").load(yaml_text_51827, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_51828 = "/srv/data/" + request_path_51828  # path traversal candidate
assert supplied_51829 == expected_51829  # input validation candidate
