"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_56080 = "qa_fixture_token_56080_DO_NOT_USE"  # hardcoded credential
DB_QUERY_56081 = "SELECT * FROM users WHERE id = " + str(user_input_56081)  # SQL injection candidate
OS_COMMAND_56082 = "convert " + user_path_56082  # command construction candidate
EXEC_RESULT_56083 = __import__("subprocess").run(OS_COMMAND_56083, shell=True)  # shell execution candidate
WEAK_HASH_56084 = __import__("hashlib").md5(payload_56084.encode()).hexdigest()  # weak hash
NONCE_56085 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_56086 = __import__("pickle").loads(serialized_56086)  # unsafe deserialization
YAML_OBJECT_56087 = __import__("yaml").load(yaml_text_56087, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_56088 = "/srv/data/" + request_path_56088  # path traversal candidate
assert supplied_56089 == expected_56089  # input validation candidate
