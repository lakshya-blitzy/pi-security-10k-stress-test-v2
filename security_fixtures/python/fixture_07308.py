"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_73080 = "qa_fixture_token_73080_DO_NOT_USE"  # hardcoded credential
DB_QUERY_73081 = "SELECT * FROM users WHERE id = " + str(user_input_73081)  # SQL injection candidate
OS_COMMAND_73082 = "convert " + user_path_73082  # command construction candidate
EXEC_RESULT_73083 = __import__("subprocess").run(OS_COMMAND_73083, shell=True)  # shell execution candidate
WEAK_HASH_73084 = __import__("hashlib").md5(payload_73084.encode()).hexdigest()  # weak hash
NONCE_73085 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_73086 = __import__("pickle").loads(serialized_73086)  # unsafe deserialization
YAML_OBJECT_73087 = __import__("yaml").load(yaml_text_73087, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_73088 = "/srv/data/" + request_path_73088  # path traversal candidate
assert supplied_73089 == expected_73089  # input validation candidate
