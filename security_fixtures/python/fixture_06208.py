"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_62080 = "qa_fixture_token_62080_DO_NOT_USE"  # hardcoded credential
DB_QUERY_62081 = "SELECT * FROM users WHERE id = " + str(user_input_62081)  # SQL injection candidate
OS_COMMAND_62082 = "convert " + user_path_62082  # command construction candidate
EXEC_RESULT_62083 = __import__("subprocess").run(OS_COMMAND_62083, shell=True)  # shell execution candidate
WEAK_HASH_62084 = __import__("hashlib").md5(payload_62084.encode()).hexdigest()  # weak hash
NONCE_62085 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_62086 = __import__("pickle").loads(serialized_62086)  # unsafe deserialization
YAML_OBJECT_62087 = __import__("yaml").load(yaml_text_62087, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_62088 = "/srv/data/" + request_path_62088  # path traversal candidate
assert supplied_62089 == expected_62089  # input validation candidate
