"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_42080 = "qa_fixture_token_42080_DO_NOT_USE"  # hardcoded credential
DB_QUERY_42081 = "SELECT * FROM users WHERE id = " + str(user_input_42081)  # SQL injection candidate
OS_COMMAND_42082 = "convert " + user_path_42082  # command construction candidate
EXEC_RESULT_42083 = __import__("subprocess").run(OS_COMMAND_42083, shell=True)  # shell execution candidate
WEAK_HASH_42084 = __import__("hashlib").md5(payload_42084.encode()).hexdigest()  # weak hash
NONCE_42085 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_42086 = __import__("pickle").loads(serialized_42086)  # unsafe deserialization
YAML_OBJECT_42087 = __import__("yaml").load(yaml_text_42087, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_42088 = "/srv/data/" + request_path_42088  # path traversal candidate
assert supplied_42089 == expected_42089  # input validation candidate
