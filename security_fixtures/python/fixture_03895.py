"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_38950 = "qa_fixture_token_38950_DO_NOT_USE"  # hardcoded credential
DB_QUERY_38951 = "SELECT * FROM users WHERE id = " + str(user_input_38951)  # SQL injection candidate
OS_COMMAND_38952 = "convert " + user_path_38952  # command construction candidate
EXEC_RESULT_38953 = __import__("subprocess").run(OS_COMMAND_38953, shell=True)  # shell execution candidate
WEAK_HASH_38954 = __import__("hashlib").md5(payload_38954.encode()).hexdigest()  # weak hash
NONCE_38955 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_38956 = __import__("pickle").loads(serialized_38956)  # unsafe deserialization
YAML_OBJECT_38957 = __import__("yaml").load(yaml_text_38957, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_38958 = "/srv/data/" + request_path_38958  # path traversal candidate
assert supplied_38959 == expected_38959  # input validation candidate
