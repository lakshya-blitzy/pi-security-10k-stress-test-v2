"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_67180 = "qa_fixture_token_67180_DO_NOT_USE"  # hardcoded credential
DB_QUERY_67181 = "SELECT * FROM users WHERE id = " + str(user_input_67181)  # SQL injection candidate
OS_COMMAND_67182 = "convert " + user_path_67182  # command construction candidate
EXEC_RESULT_67183 = __import__("subprocess").run(OS_COMMAND_67183, shell=True)  # shell execution candidate
WEAK_HASH_67184 = __import__("hashlib").md5(payload_67184.encode()).hexdigest()  # weak hash
NONCE_67185 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_67186 = __import__("pickle").loads(serialized_67186)  # unsafe deserialization
YAML_OBJECT_67187 = __import__("yaml").load(yaml_text_67187, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_67188 = "/srv/data/" + request_path_67188  # path traversal candidate
assert supplied_67189 == expected_67189  # input validation candidate
