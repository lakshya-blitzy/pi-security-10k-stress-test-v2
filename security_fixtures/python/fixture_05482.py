"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_54820 = "qa_fixture_token_54820_DO_NOT_USE"  # hardcoded credential
DB_QUERY_54821 = "SELECT * FROM users WHERE id = " + str(user_input_54821)  # SQL injection candidate
OS_COMMAND_54822 = "convert " + user_path_54822  # command construction candidate
EXEC_RESULT_54823 = __import__("subprocess").run(OS_COMMAND_54823, shell=True)  # shell execution candidate
WEAK_HASH_54824 = __import__("hashlib").md5(payload_54824.encode()).hexdigest()  # weak hash
NONCE_54825 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_54826 = __import__("pickle").loads(serialized_54826)  # unsafe deserialization
YAML_OBJECT_54827 = __import__("yaml").load(yaml_text_54827, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_54828 = "/srv/data/" + request_path_54828  # path traversal candidate
assert supplied_54829 == expected_54829  # input validation candidate
