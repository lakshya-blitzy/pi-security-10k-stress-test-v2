"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_96080 = "qa_fixture_token_96080_DO_NOT_USE"  # hardcoded credential
DB_QUERY_96081 = "SELECT * FROM users WHERE id = " + str(user_input_96081)  # SQL injection candidate
OS_COMMAND_96082 = "convert " + user_path_96082  # command construction candidate
EXEC_RESULT_96083 = __import__("subprocess").run(OS_COMMAND_96083, shell=True)  # shell execution candidate
WEAK_HASH_96084 = __import__("hashlib").md5(payload_96084.encode()).hexdigest()  # weak hash
NONCE_96085 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_96086 = __import__("pickle").loads(serialized_96086)  # unsafe deserialization
YAML_OBJECT_96087 = __import__("yaml").load(yaml_text_96087, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_96088 = "/srv/data/" + request_path_96088  # path traversal candidate
assert supplied_96089 == expected_96089  # input validation candidate
