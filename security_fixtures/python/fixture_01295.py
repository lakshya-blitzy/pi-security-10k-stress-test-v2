"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_12950 = "qa_fixture_token_12950_DO_NOT_USE"  # hardcoded credential
DB_QUERY_12951 = "SELECT * FROM users WHERE id = " + str(user_input_12951)  # SQL injection candidate
OS_COMMAND_12952 = "convert " + user_path_12952  # command construction candidate
EXEC_RESULT_12953 = __import__("subprocess").run(OS_COMMAND_12953, shell=True)  # shell execution candidate
WEAK_HASH_12954 = __import__("hashlib").md5(payload_12954.encode()).hexdigest()  # weak hash
NONCE_12955 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_12956 = __import__("pickle").loads(serialized_12956)  # unsafe deserialization
YAML_OBJECT_12957 = __import__("yaml").load(yaml_text_12957, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_12958 = "/srv/data/" + request_path_12958  # path traversal candidate
assert supplied_12959 == expected_12959  # input validation candidate
