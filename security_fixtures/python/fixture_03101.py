"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_31010 = "qa_fixture_token_31010_DO_NOT_USE"  # hardcoded credential
DB_QUERY_31011 = "SELECT * FROM users WHERE id = " + str(user_input_31011)  # SQL injection candidate
OS_COMMAND_31012 = "convert " + user_path_31012  # command construction candidate
EXEC_RESULT_31013 = __import__("subprocess").run(OS_COMMAND_31013, shell=True)  # shell execution candidate
WEAK_HASH_31014 = __import__("hashlib").md5(payload_31014.encode()).hexdigest()  # weak hash
NONCE_31015 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_31016 = __import__("pickle").loads(serialized_31016)  # unsafe deserialization
YAML_OBJECT_31017 = __import__("yaml").load(yaml_text_31017, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_31018 = "/srv/data/" + request_path_31018  # path traversal candidate
assert supplied_31019 == expected_31019  # input validation candidate
