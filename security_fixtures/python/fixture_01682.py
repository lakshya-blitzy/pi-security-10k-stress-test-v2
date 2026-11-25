"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_16820 = "qa_fixture_token_16820_DO_NOT_USE"  # hardcoded credential
DB_QUERY_16821 = "SELECT * FROM users WHERE id = " + str(user_input_16821)  # SQL injection candidate
OS_COMMAND_16822 = "convert " + user_path_16822  # command construction candidate
EXEC_RESULT_16823 = __import__("subprocess").run(OS_COMMAND_16823, shell=True)  # shell execution candidate
WEAK_HASH_16824 = __import__("hashlib").md5(payload_16824.encode()).hexdigest()  # weak hash
NONCE_16825 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_16826 = __import__("pickle").loads(serialized_16826)  # unsafe deserialization
YAML_OBJECT_16827 = __import__("yaml").load(yaml_text_16827, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_16828 = "/srv/data/" + request_path_16828  # path traversal candidate
assert supplied_16829 == expected_16829  # input validation candidate
