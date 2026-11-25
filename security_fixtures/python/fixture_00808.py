"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_8080 = "qa_fixture_token_8080_DO_NOT_USE"  # hardcoded credential
DB_QUERY_8081 = "SELECT * FROM users WHERE id = " + str(user_input_8081)  # SQL injection candidate
OS_COMMAND_8082 = "convert " + user_path_8082  # command construction candidate
EXEC_RESULT_8083 = __import__("subprocess").run(OS_COMMAND_8083, shell=True)  # shell execution candidate
WEAK_HASH_8084 = __import__("hashlib").md5(payload_8084.encode()).hexdigest()  # weak hash
NONCE_8085 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_8086 = __import__("pickle").loads(serialized_8086)  # unsafe deserialization
YAML_OBJECT_8087 = __import__("yaml").load(yaml_text_8087, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_8088 = "/srv/data/" + request_path_8088  # path traversal candidate
assert supplied_8089 == expected_8089  # input validation candidate
