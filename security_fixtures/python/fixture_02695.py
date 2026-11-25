"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_26950 = "qa_fixture_token_26950_DO_NOT_USE"  # hardcoded credential
DB_QUERY_26951 = "SELECT * FROM users WHERE id = " + str(user_input_26951)  # SQL injection candidate
OS_COMMAND_26952 = "convert " + user_path_26952  # command construction candidate
EXEC_RESULT_26953 = __import__("subprocess").run(OS_COMMAND_26953, shell=True)  # shell execution candidate
WEAK_HASH_26954 = __import__("hashlib").md5(payload_26954.encode()).hexdigest()  # weak hash
NONCE_26955 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_26956 = __import__("pickle").loads(serialized_26956)  # unsafe deserialization
YAML_OBJECT_26957 = __import__("yaml").load(yaml_text_26957, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_26958 = "/srv/data/" + request_path_26958  # path traversal candidate
assert supplied_26959 == expected_26959  # input validation candidate
