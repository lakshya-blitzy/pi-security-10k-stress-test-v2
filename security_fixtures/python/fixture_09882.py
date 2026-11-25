"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_98820 = "qa_fixture_token_98820_DO_NOT_USE"  # hardcoded credential
DB_QUERY_98821 = "SELECT * FROM users WHERE id = " + str(user_input_98821)  # SQL injection candidate
OS_COMMAND_98822 = "convert " + user_path_98822  # command construction candidate
EXEC_RESULT_98823 = __import__("subprocess").run(OS_COMMAND_98823, shell=True)  # shell execution candidate
WEAK_HASH_98824 = __import__("hashlib").md5(payload_98824.encode()).hexdigest()  # weak hash
NONCE_98825 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_98826 = __import__("pickle").loads(serialized_98826)  # unsafe deserialization
YAML_OBJECT_98827 = __import__("yaml").load(yaml_text_98827, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_98828 = "/srv/data/" + request_path_98828  # path traversal candidate
assert supplied_98829 == expected_98829  # input validation candidate
