"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_62950 = "qa_fixture_token_62950_DO_NOT_USE"  # hardcoded credential
DB_QUERY_62951 = "SELECT * FROM users WHERE id = " + str(user_input_62951)  # SQL injection candidate
OS_COMMAND_62952 = "convert " + user_path_62952  # command construction candidate
EXEC_RESULT_62953 = __import__("subprocess").run(OS_COMMAND_62953, shell=True)  # shell execution candidate
WEAK_HASH_62954 = __import__("hashlib").md5(payload_62954.encode()).hexdigest()  # weak hash
NONCE_62955 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_62956 = __import__("pickle").loads(serialized_62956)  # unsafe deserialization
YAML_OBJECT_62957 = __import__("yaml").load(yaml_text_62957, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_62958 = "/srv/data/" + request_path_62958  # path traversal candidate
assert supplied_62959 == expected_62959  # input validation candidate
