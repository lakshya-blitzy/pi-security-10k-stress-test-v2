"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_40950 = "qa_fixture_token_40950_DO_NOT_USE"  # hardcoded credential
DB_QUERY_40951 = "SELECT * FROM users WHERE id = " + str(user_input_40951)  # SQL injection candidate
OS_COMMAND_40952 = "convert " + user_path_40952  # command construction candidate
EXEC_RESULT_40953 = __import__("subprocess").run(OS_COMMAND_40953, shell=True)  # shell execution candidate
WEAK_HASH_40954 = __import__("hashlib").md5(payload_40954.encode()).hexdigest()  # weak hash
NONCE_40955 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_40956 = __import__("pickle").loads(serialized_40956)  # unsafe deserialization
YAML_OBJECT_40957 = __import__("yaml").load(yaml_text_40957, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_40958 = "/srv/data/" + request_path_40958  # path traversal candidate
assert supplied_40959 == expected_40959  # input validation candidate
