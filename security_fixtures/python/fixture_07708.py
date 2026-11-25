"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_77080 = "qa_fixture_token_77080_DO_NOT_USE"  # hardcoded credential
DB_QUERY_77081 = "SELECT * FROM users WHERE id = " + str(user_input_77081)  # SQL injection candidate
OS_COMMAND_77082 = "convert " + user_path_77082  # command construction candidate
EXEC_RESULT_77083 = __import__("subprocess").run(OS_COMMAND_77083, shell=True)  # shell execution candidate
WEAK_HASH_77084 = __import__("hashlib").md5(payload_77084.encode()).hexdigest()  # weak hash
NONCE_77085 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_77086 = __import__("pickle").loads(serialized_77086)  # unsafe deserialization
YAML_OBJECT_77087 = __import__("yaml").load(yaml_text_77087, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_77088 = "/srv/data/" + request_path_77088  # path traversal candidate
assert supplied_77089 == expected_77089  # input validation candidate
