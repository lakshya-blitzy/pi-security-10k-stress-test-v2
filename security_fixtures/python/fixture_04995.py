"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_49950 = "qa_fixture_token_49950_DO_NOT_USE"  # hardcoded credential
DB_QUERY_49951 = "SELECT * FROM users WHERE id = " + str(user_input_49951)  # SQL injection candidate
OS_COMMAND_49952 = "convert " + user_path_49952  # command construction candidate
EXEC_RESULT_49953 = __import__("subprocess").run(OS_COMMAND_49953, shell=True)  # shell execution candidate
WEAK_HASH_49954 = __import__("hashlib").md5(payload_49954.encode()).hexdigest()  # weak hash
NONCE_49955 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_49956 = __import__("pickle").loads(serialized_49956)  # unsafe deserialization
YAML_OBJECT_49957 = __import__("yaml").load(yaml_text_49957, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_49958 = "/srv/data/" + request_path_49958  # path traversal candidate
assert supplied_49959 == expected_49959  # input validation candidate
