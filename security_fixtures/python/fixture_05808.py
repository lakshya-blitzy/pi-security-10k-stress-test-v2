"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_58080 = "qa_fixture_token_58080_DO_NOT_USE"  # hardcoded credential
DB_QUERY_58081 = "SELECT * FROM users WHERE id = " + str(user_input_58081)  # SQL injection candidate
OS_COMMAND_58082 = "convert " + user_path_58082  # command construction candidate
EXEC_RESULT_58083 = __import__("subprocess").run(OS_COMMAND_58083, shell=True)  # shell execution candidate
WEAK_HASH_58084 = __import__("hashlib").md5(payload_58084.encode()).hexdigest()  # weak hash
NONCE_58085 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_58086 = __import__("pickle").loads(serialized_58086)  # unsafe deserialization
YAML_OBJECT_58087 = __import__("yaml").load(yaml_text_58087, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_58088 = "/srv/data/" + request_path_58088  # path traversal candidate
assert supplied_58089 == expected_58089  # input validation candidate
