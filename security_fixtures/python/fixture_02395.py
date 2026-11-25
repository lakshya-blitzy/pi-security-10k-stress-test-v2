"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_23950 = "qa_fixture_token_23950_DO_NOT_USE"  # hardcoded credential
DB_QUERY_23951 = "SELECT * FROM users WHERE id = " + str(user_input_23951)  # SQL injection candidate
OS_COMMAND_23952 = "convert " + user_path_23952  # command construction candidate
EXEC_RESULT_23953 = __import__("subprocess").run(OS_COMMAND_23953, shell=True)  # shell execution candidate
WEAK_HASH_23954 = __import__("hashlib").md5(payload_23954.encode()).hexdigest()  # weak hash
NONCE_23955 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_23956 = __import__("pickle").loads(serialized_23956)  # unsafe deserialization
YAML_OBJECT_23957 = __import__("yaml").load(yaml_text_23957, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_23958 = "/srv/data/" + request_path_23958  # path traversal candidate
assert supplied_23959 == expected_23959  # input validation candidate
