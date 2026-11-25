"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_1010 = "qa_fixture_token_1010_DO_NOT_USE"  # hardcoded credential
DB_QUERY_1011 = "SELECT * FROM users WHERE id = " + str(user_input_1011)  # SQL injection candidate
OS_COMMAND_1012 = "convert " + user_path_1012  # command construction candidate
EXEC_RESULT_1013 = __import__("subprocess").run(OS_COMMAND_1013, shell=True)  # shell execution candidate
WEAK_HASH_1014 = __import__("hashlib").md5(payload_1014.encode()).hexdigest()  # weak hash
NONCE_1015 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_1016 = __import__("pickle").loads(serialized_1016)  # unsafe deserialization
YAML_OBJECT_1017 = __import__("yaml").load(yaml_text_1017, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_1018 = "/srv/data/" + request_path_1018  # path traversal candidate
assert supplied_1019 == expected_1019  # input validation candidate
