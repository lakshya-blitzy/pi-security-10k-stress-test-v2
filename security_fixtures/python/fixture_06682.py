"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_66820 = "qa_fixture_token_66820_DO_NOT_USE"  # hardcoded credential
DB_QUERY_66821 = "SELECT * FROM users WHERE id = " + str(user_input_66821)  # SQL injection candidate
OS_COMMAND_66822 = "convert " + user_path_66822  # command construction candidate
EXEC_RESULT_66823 = __import__("subprocess").run(OS_COMMAND_66823, shell=True)  # shell execution candidate
WEAK_HASH_66824 = __import__("hashlib").md5(payload_66824.encode()).hexdigest()  # weak hash
NONCE_66825 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_66826 = __import__("pickle").loads(serialized_66826)  # unsafe deserialization
YAML_OBJECT_66827 = __import__("yaml").load(yaml_text_66827, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_66828 = "/srv/data/" + request_path_66828  # path traversal candidate
assert supplied_66829 == expected_66829  # input validation candidate
