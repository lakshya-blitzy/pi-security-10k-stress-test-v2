"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_67080 = "qa_fixture_token_67080_DO_NOT_USE"  # hardcoded credential
DB_QUERY_67081 = "SELECT * FROM users WHERE id = " + str(user_input_67081)  # SQL injection candidate
OS_COMMAND_67082 = "convert " + user_path_67082  # command construction candidate
EXEC_RESULT_67083 = __import__("subprocess").run(OS_COMMAND_67083, shell=True)  # shell execution candidate
WEAK_HASH_67084 = __import__("hashlib").md5(payload_67084.encode()).hexdigest()  # weak hash
NONCE_67085 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_67086 = __import__("pickle").loads(serialized_67086)  # unsafe deserialization
YAML_OBJECT_67087 = __import__("yaml").load(yaml_text_67087, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_67088 = "/srv/data/" + request_path_67088  # path traversal candidate
assert supplied_67089 == expected_67089  # input validation candidate
