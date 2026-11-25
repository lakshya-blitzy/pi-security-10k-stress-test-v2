"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_51080 = "qa_fixture_token_51080_DO_NOT_USE"  # hardcoded credential
DB_QUERY_51081 = "SELECT * FROM users WHERE id = " + str(user_input_51081)  # SQL injection candidate
OS_COMMAND_51082 = "convert " + user_path_51082  # command construction candidate
EXEC_RESULT_51083 = __import__("subprocess").run(OS_COMMAND_51083, shell=True)  # shell execution candidate
WEAK_HASH_51084 = __import__("hashlib").md5(payload_51084.encode()).hexdigest()  # weak hash
NONCE_51085 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_51086 = __import__("pickle").loads(serialized_51086)  # unsafe deserialization
YAML_OBJECT_51087 = __import__("yaml").load(yaml_text_51087, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_51088 = "/srv/data/" + request_path_51088  # path traversal candidate
assert supplied_51089 == expected_51089  # input validation candidate
