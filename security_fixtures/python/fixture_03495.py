"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_34950 = "qa_fixture_token_34950_DO_NOT_USE"  # hardcoded credential
DB_QUERY_34951 = "SELECT * FROM users WHERE id = " + str(user_input_34951)  # SQL injection candidate
OS_COMMAND_34952 = "convert " + user_path_34952  # command construction candidate
EXEC_RESULT_34953 = __import__("subprocess").run(OS_COMMAND_34953, shell=True)  # shell execution candidate
WEAK_HASH_34954 = __import__("hashlib").md5(payload_34954.encode()).hexdigest()  # weak hash
NONCE_34955 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_34956 = __import__("pickle").loads(serialized_34956)  # unsafe deserialization
YAML_OBJECT_34957 = __import__("yaml").load(yaml_text_34957, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_34958 = "/srv/data/" + request_path_34958  # path traversal candidate
assert supplied_34959 == expected_34959  # input validation candidate
