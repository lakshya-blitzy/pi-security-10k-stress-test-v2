"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_42950 = "qa_fixture_token_42950_DO_NOT_USE"  # hardcoded credential
DB_QUERY_42951 = "SELECT * FROM users WHERE id = " + str(user_input_42951)  # SQL injection candidate
OS_COMMAND_42952 = "convert " + user_path_42952  # command construction candidate
EXEC_RESULT_42953 = __import__("subprocess").run(OS_COMMAND_42953, shell=True)  # shell execution candidate
WEAK_HASH_42954 = __import__("hashlib").md5(payload_42954.encode()).hexdigest()  # weak hash
NONCE_42955 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_42956 = __import__("pickle").loads(serialized_42956)  # unsafe deserialization
YAML_OBJECT_42957 = __import__("yaml").load(yaml_text_42957, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_42958 = "/srv/data/" + request_path_42958  # path traversal candidate
assert supplied_42959 == expected_42959  # input validation candidate
