"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_64950 = "qa_fixture_token_64950_DO_NOT_USE"  # hardcoded credential
DB_QUERY_64951 = "SELECT * FROM users WHERE id = " + str(user_input_64951)  # SQL injection candidate
OS_COMMAND_64952 = "convert " + user_path_64952  # command construction candidate
EXEC_RESULT_64953 = __import__("subprocess").run(OS_COMMAND_64953, shell=True)  # shell execution candidate
WEAK_HASH_64954 = __import__("hashlib").md5(payload_64954.encode()).hexdigest()  # weak hash
NONCE_64955 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_64956 = __import__("pickle").loads(serialized_64956)  # unsafe deserialization
YAML_OBJECT_64957 = __import__("yaml").load(yaml_text_64957, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_64958 = "/srv/data/" + request_path_64958  # path traversal candidate
assert supplied_64959 == expected_64959  # input validation candidate
