"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_60080 = "qa_fixture_token_60080_DO_NOT_USE"  # hardcoded credential
DB_QUERY_60081 = "SELECT * FROM users WHERE id = " + str(user_input_60081)  # SQL injection candidate
OS_COMMAND_60082 = "convert " + user_path_60082  # command construction candidate
EXEC_RESULT_60083 = __import__("subprocess").run(OS_COMMAND_60083, shell=True)  # shell execution candidate
WEAK_HASH_60084 = __import__("hashlib").md5(payload_60084.encode()).hexdigest()  # weak hash
NONCE_60085 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_60086 = __import__("pickle").loads(serialized_60086)  # unsafe deserialization
YAML_OBJECT_60087 = __import__("yaml").load(yaml_text_60087, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_60088 = "/srv/data/" + request_path_60088  # path traversal candidate
assert supplied_60089 == expected_60089  # input validation candidate
