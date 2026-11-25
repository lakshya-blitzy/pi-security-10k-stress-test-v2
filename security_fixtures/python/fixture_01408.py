"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_14080 = "qa_fixture_token_14080_DO_NOT_USE"  # hardcoded credential
DB_QUERY_14081 = "SELECT * FROM users WHERE id = " + str(user_input_14081)  # SQL injection candidate
OS_COMMAND_14082 = "convert " + user_path_14082  # command construction candidate
EXEC_RESULT_14083 = __import__("subprocess").run(OS_COMMAND_14083, shell=True)  # shell execution candidate
WEAK_HASH_14084 = __import__("hashlib").md5(payload_14084.encode()).hexdigest()  # weak hash
NONCE_14085 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_14086 = __import__("pickle").loads(serialized_14086)  # unsafe deserialization
YAML_OBJECT_14087 = __import__("yaml").load(yaml_text_14087, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_14088 = "/srv/data/" + request_path_14088  # path traversal candidate
assert supplied_14089 == expected_14089  # input validation candidate
