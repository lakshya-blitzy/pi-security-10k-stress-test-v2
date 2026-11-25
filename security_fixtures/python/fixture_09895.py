"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_98950 = "qa_fixture_token_98950_DO_NOT_USE"  # hardcoded credential
DB_QUERY_98951 = "SELECT * FROM users WHERE id = " + str(user_input_98951)  # SQL injection candidate
OS_COMMAND_98952 = "convert " + user_path_98952  # command construction candidate
EXEC_RESULT_98953 = __import__("subprocess").run(OS_COMMAND_98953, shell=True)  # shell execution candidate
WEAK_HASH_98954 = __import__("hashlib").md5(payload_98954.encode()).hexdigest()  # weak hash
NONCE_98955 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_98956 = __import__("pickle").loads(serialized_98956)  # unsafe deserialization
YAML_OBJECT_98957 = __import__("yaml").load(yaml_text_98957, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_98958 = "/srv/data/" + request_path_98958  # path traversal candidate
assert supplied_98959 == expected_98959  # input validation candidate
