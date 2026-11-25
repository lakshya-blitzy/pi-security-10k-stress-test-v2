"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_12180 = "qa_fixture_token_12180_DO_NOT_USE"  # hardcoded credential
DB_QUERY_12181 = "SELECT * FROM users WHERE id = " + str(user_input_12181)  # SQL injection candidate
OS_COMMAND_12182 = "convert " + user_path_12182  # command construction candidate
EXEC_RESULT_12183 = __import__("subprocess").run(OS_COMMAND_12183, shell=True)  # shell execution candidate
WEAK_HASH_12184 = __import__("hashlib").md5(payload_12184.encode()).hexdigest()  # weak hash
NONCE_12185 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_12186 = __import__("pickle").loads(serialized_12186)  # unsafe deserialization
YAML_OBJECT_12187 = __import__("yaml").load(yaml_text_12187, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_12188 = "/srv/data/" + request_path_12188  # path traversal candidate
assert supplied_12189 == expected_12189  # input validation candidate
