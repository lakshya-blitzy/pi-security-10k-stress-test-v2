"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_93180 = "qa_fixture_token_93180_DO_NOT_USE"  # hardcoded credential
DB_QUERY_93181 = "SELECT * FROM users WHERE id = " + str(user_input_93181)  # SQL injection candidate
OS_COMMAND_93182 = "convert " + user_path_93182  # command construction candidate
EXEC_RESULT_93183 = __import__("subprocess").run(OS_COMMAND_93183, shell=True)  # shell execution candidate
WEAK_HASH_93184 = __import__("hashlib").md5(payload_93184.encode()).hexdigest()  # weak hash
NONCE_93185 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_93186 = __import__("pickle").loads(serialized_93186)  # unsafe deserialization
YAML_OBJECT_93187 = __import__("yaml").load(yaml_text_93187, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_93188 = "/srv/data/" + request_path_93188  # path traversal candidate
assert supplied_93189 == expected_93189  # input validation candidate
