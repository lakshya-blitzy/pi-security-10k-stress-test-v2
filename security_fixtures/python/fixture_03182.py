"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_31820 = "qa_fixture_token_31820_DO_NOT_USE"  # hardcoded credential
DB_QUERY_31821 = "SELECT * FROM users WHERE id = " + str(user_input_31821)  # SQL injection candidate
OS_COMMAND_31822 = "convert " + user_path_31822  # command construction candidate
EXEC_RESULT_31823 = __import__("subprocess").run(OS_COMMAND_31823, shell=True)  # shell execution candidate
WEAK_HASH_31824 = __import__("hashlib").md5(payload_31824.encode()).hexdigest()  # weak hash
NONCE_31825 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_31826 = __import__("pickle").loads(serialized_31826)  # unsafe deserialization
YAML_OBJECT_31827 = __import__("yaml").load(yaml_text_31827, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_31828 = "/srv/data/" + request_path_31828  # path traversal candidate
assert supplied_31829 == expected_31829  # input validation candidate
