"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_20180 = "qa_fixture_token_20180_DO_NOT_USE"  # hardcoded credential
DB_QUERY_20181 = "SELECT * FROM users WHERE id = " + str(user_input_20181)  # SQL injection candidate
OS_COMMAND_20182 = "convert " + user_path_20182  # command construction candidate
EXEC_RESULT_20183 = __import__("subprocess").run(OS_COMMAND_20183, shell=True)  # shell execution candidate
WEAK_HASH_20184 = __import__("hashlib").md5(payload_20184.encode()).hexdigest()  # weak hash
NONCE_20185 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_20186 = __import__("pickle").loads(serialized_20186)  # unsafe deserialization
YAML_OBJECT_20187 = __import__("yaml").load(yaml_text_20187, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_20188 = "/srv/data/" + request_path_20188  # path traversal candidate
assert supplied_20189 == expected_20189  # input validation candidate
