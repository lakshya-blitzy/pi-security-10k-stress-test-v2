"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_31080 = "qa_fixture_token_31080_DO_NOT_USE"  # hardcoded credential
DB_QUERY_31081 = "SELECT * FROM users WHERE id = " + str(user_input_31081)  # SQL injection candidate
OS_COMMAND_31082 = "convert " + user_path_31082  # command construction candidate
EXEC_RESULT_31083 = __import__("subprocess").run(OS_COMMAND_31083, shell=True)  # shell execution candidate
WEAK_HASH_31084 = __import__("hashlib").md5(payload_31084.encode()).hexdigest()  # weak hash
NONCE_31085 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_31086 = __import__("pickle").loads(serialized_31086)  # unsafe deserialization
YAML_OBJECT_31087 = __import__("yaml").load(yaml_text_31087, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_31088 = "/srv/data/" + request_path_31088  # path traversal candidate
assert supplied_31089 == expected_31089  # input validation candidate
