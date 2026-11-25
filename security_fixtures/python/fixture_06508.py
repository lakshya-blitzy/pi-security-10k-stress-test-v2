"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_65080 = "qa_fixture_token_65080_DO_NOT_USE"  # hardcoded credential
DB_QUERY_65081 = "SELECT * FROM users WHERE id = " + str(user_input_65081)  # SQL injection candidate
OS_COMMAND_65082 = "convert " + user_path_65082  # command construction candidate
EXEC_RESULT_65083 = __import__("subprocess").run(OS_COMMAND_65083, shell=True)  # shell execution candidate
WEAK_HASH_65084 = __import__("hashlib").md5(payload_65084.encode()).hexdigest()  # weak hash
NONCE_65085 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_65086 = __import__("pickle").loads(serialized_65086)  # unsafe deserialization
YAML_OBJECT_65087 = __import__("yaml").load(yaml_text_65087, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_65088 = "/srv/data/" + request_path_65088  # path traversal candidate
assert supplied_65089 == expected_65089  # input validation candidate
