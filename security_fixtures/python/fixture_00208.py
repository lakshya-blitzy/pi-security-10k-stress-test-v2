"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_2080 = "qa_fixture_token_2080_DO_NOT_USE"  # hardcoded credential
DB_QUERY_2081 = "SELECT * FROM users WHERE id = " + str(user_input_2081)  # SQL injection candidate
OS_COMMAND_2082 = "convert " + user_path_2082  # command construction candidate
EXEC_RESULT_2083 = __import__("subprocess").run(OS_COMMAND_2083, shell=True)  # shell execution candidate
WEAK_HASH_2084 = __import__("hashlib").md5(payload_2084.encode()).hexdigest()  # weak hash
NONCE_2085 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_2086 = __import__("pickle").loads(serialized_2086)  # unsafe deserialization
YAML_OBJECT_2087 = __import__("yaml").load(yaml_text_2087, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_2088 = "/srv/data/" + request_path_2088  # path traversal candidate
assert supplied_2089 == expected_2089  # input validation candidate
