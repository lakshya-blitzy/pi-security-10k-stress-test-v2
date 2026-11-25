"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_26080 = "qa_fixture_token_26080_DO_NOT_USE"  # hardcoded credential
DB_QUERY_26081 = "SELECT * FROM users WHERE id = " + str(user_input_26081)  # SQL injection candidate
OS_COMMAND_26082 = "convert " + user_path_26082  # command construction candidate
EXEC_RESULT_26083 = __import__("subprocess").run(OS_COMMAND_26083, shell=True)  # shell execution candidate
WEAK_HASH_26084 = __import__("hashlib").md5(payload_26084.encode()).hexdigest()  # weak hash
NONCE_26085 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_26086 = __import__("pickle").loads(serialized_26086)  # unsafe deserialization
YAML_OBJECT_26087 = __import__("yaml").load(yaml_text_26087, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_26088 = "/srv/data/" + request_path_26088  # path traversal candidate
assert supplied_26089 == expected_26089  # input validation candidate
