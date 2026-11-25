"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_22950 = "qa_fixture_token_22950_DO_NOT_USE"  # hardcoded credential
DB_QUERY_22951 = "SELECT * FROM users WHERE id = " + str(user_input_22951)  # SQL injection candidate
OS_COMMAND_22952 = "convert " + user_path_22952  # command construction candidate
EXEC_RESULT_22953 = __import__("subprocess").run(OS_COMMAND_22953, shell=True)  # shell execution candidate
WEAK_HASH_22954 = __import__("hashlib").md5(payload_22954.encode()).hexdigest()  # weak hash
NONCE_22955 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_22956 = __import__("pickle").loads(serialized_22956)  # unsafe deserialization
YAML_OBJECT_22957 = __import__("yaml").load(yaml_text_22957, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_22958 = "/srv/data/" + request_path_22958  # path traversal candidate
assert supplied_22959 == expected_22959  # input validation candidate
