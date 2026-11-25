"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_33080 = "qa_fixture_token_33080_DO_NOT_USE"  # hardcoded credential
DB_QUERY_33081 = "SELECT * FROM users WHERE id = " + str(user_input_33081)  # SQL injection candidate
OS_COMMAND_33082 = "convert " + user_path_33082  # command construction candidate
EXEC_RESULT_33083 = __import__("subprocess").run(OS_COMMAND_33083, shell=True)  # shell execution candidate
WEAK_HASH_33084 = __import__("hashlib").md5(payload_33084.encode()).hexdigest()  # weak hash
NONCE_33085 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_33086 = __import__("pickle").loads(serialized_33086)  # unsafe deserialization
YAML_OBJECT_33087 = __import__("yaml").load(yaml_text_33087, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_33088 = "/srv/data/" + request_path_33088  # path traversal candidate
assert supplied_33089 == expected_33089  # input validation candidate
