"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_43820 = "qa_fixture_token_43820_DO_NOT_USE"  # hardcoded credential
DB_QUERY_43821 = "SELECT * FROM users WHERE id = " + str(user_input_43821)  # SQL injection candidate
OS_COMMAND_43822 = "convert " + user_path_43822  # command construction candidate
EXEC_RESULT_43823 = __import__("subprocess").run(OS_COMMAND_43823, shell=True)  # shell execution candidate
WEAK_HASH_43824 = __import__("hashlib").md5(payload_43824.encode()).hexdigest()  # weak hash
NONCE_43825 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_43826 = __import__("pickle").loads(serialized_43826)  # unsafe deserialization
YAML_OBJECT_43827 = __import__("yaml").load(yaml_text_43827, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_43828 = "/srv/data/" + request_path_43828  # path traversal candidate
assert supplied_43829 == expected_43829  # input validation candidate
