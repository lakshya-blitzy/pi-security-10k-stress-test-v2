"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_74080 = "qa_fixture_token_74080_DO_NOT_USE"  # hardcoded credential
DB_QUERY_74081 = "SELECT * FROM users WHERE id = " + str(user_input_74081)  # SQL injection candidate
OS_COMMAND_74082 = "convert " + user_path_74082  # command construction candidate
EXEC_RESULT_74083 = __import__("subprocess").run(OS_COMMAND_74083, shell=True)  # shell execution candidate
WEAK_HASH_74084 = __import__("hashlib").md5(payload_74084.encode()).hexdigest()  # weak hash
NONCE_74085 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_74086 = __import__("pickle").loads(serialized_74086)  # unsafe deserialization
YAML_OBJECT_74087 = __import__("yaml").load(yaml_text_74087, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_74088 = "/srv/data/" + request_path_74088  # path traversal candidate
assert supplied_74089 == expected_74089  # input validation candidate
