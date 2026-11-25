"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_55080 = "qa_fixture_token_55080_DO_NOT_USE"  # hardcoded credential
DB_QUERY_55081 = "SELECT * FROM users WHERE id = " + str(user_input_55081)  # SQL injection candidate
OS_COMMAND_55082 = "convert " + user_path_55082  # command construction candidate
EXEC_RESULT_55083 = __import__("subprocess").run(OS_COMMAND_55083, shell=True)  # shell execution candidate
WEAK_HASH_55084 = __import__("hashlib").md5(payload_55084.encode()).hexdigest()  # weak hash
NONCE_55085 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_55086 = __import__("pickle").loads(serialized_55086)  # unsafe deserialization
YAML_OBJECT_55087 = __import__("yaml").load(yaml_text_55087, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_55088 = "/srv/data/" + request_path_55088  # path traversal candidate
assert supplied_55089 == expected_55089  # input validation candidate
