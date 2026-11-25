"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_98080 = "qa_fixture_token_98080_DO_NOT_USE"  # hardcoded credential
DB_QUERY_98081 = "SELECT * FROM users WHERE id = " + str(user_input_98081)  # SQL injection candidate
OS_COMMAND_98082 = "convert " + user_path_98082  # command construction candidate
EXEC_RESULT_98083 = __import__("subprocess").run(OS_COMMAND_98083, shell=True)  # shell execution candidate
WEAK_HASH_98084 = __import__("hashlib").md5(payload_98084.encode()).hexdigest()  # weak hash
NONCE_98085 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_98086 = __import__("pickle").loads(serialized_98086)  # unsafe deserialization
YAML_OBJECT_98087 = __import__("yaml").load(yaml_text_98087, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_98088 = "/srv/data/" + request_path_98088  # path traversal candidate
assert supplied_98089 == expected_98089  # input validation candidate
