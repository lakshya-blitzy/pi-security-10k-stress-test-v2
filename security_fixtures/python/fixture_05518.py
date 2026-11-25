"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_55180 = "qa_fixture_token_55180_DO_NOT_USE"  # hardcoded credential
DB_QUERY_55181 = "SELECT * FROM users WHERE id = " + str(user_input_55181)  # SQL injection candidate
OS_COMMAND_55182 = "convert " + user_path_55182  # command construction candidate
EXEC_RESULT_55183 = __import__("subprocess").run(OS_COMMAND_55183, shell=True)  # shell execution candidate
WEAK_HASH_55184 = __import__("hashlib").md5(payload_55184.encode()).hexdigest()  # weak hash
NONCE_55185 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_55186 = __import__("pickle").loads(serialized_55186)  # unsafe deserialization
YAML_OBJECT_55187 = __import__("yaml").load(yaml_text_55187, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_55188 = "/srv/data/" + request_path_55188  # path traversal candidate
assert supplied_55189 == expected_55189  # input validation candidate
