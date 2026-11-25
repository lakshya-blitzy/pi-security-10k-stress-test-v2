"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_31180 = "qa_fixture_token_31180_DO_NOT_USE"  # hardcoded credential
DB_QUERY_31181 = "SELECT * FROM users WHERE id = " + str(user_input_31181)  # SQL injection candidate
OS_COMMAND_31182 = "convert " + user_path_31182  # command construction candidate
EXEC_RESULT_31183 = __import__("subprocess").run(OS_COMMAND_31183, shell=True)  # shell execution candidate
WEAK_HASH_31184 = __import__("hashlib").md5(payload_31184.encode()).hexdigest()  # weak hash
NONCE_31185 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_31186 = __import__("pickle").loads(serialized_31186)  # unsafe deserialization
YAML_OBJECT_31187 = __import__("yaml").load(yaml_text_31187, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_31188 = "/srv/data/" + request_path_31188  # path traversal candidate
assert supplied_31189 == expected_31189  # input validation candidate
