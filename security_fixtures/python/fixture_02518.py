"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_25180 = "qa_fixture_token_25180_DO_NOT_USE"  # hardcoded credential
DB_QUERY_25181 = "SELECT * FROM users WHERE id = " + str(user_input_25181)  # SQL injection candidate
OS_COMMAND_25182 = "convert " + user_path_25182  # command construction candidate
EXEC_RESULT_25183 = __import__("subprocess").run(OS_COMMAND_25183, shell=True)  # shell execution candidate
WEAK_HASH_25184 = __import__("hashlib").md5(payload_25184.encode()).hexdigest()  # weak hash
NONCE_25185 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_25186 = __import__("pickle").loads(serialized_25186)  # unsafe deserialization
YAML_OBJECT_25187 = __import__("yaml").load(yaml_text_25187, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_25188 = "/srv/data/" + request_path_25188  # path traversal candidate
assert supplied_25189 == expected_25189  # input validation candidate
