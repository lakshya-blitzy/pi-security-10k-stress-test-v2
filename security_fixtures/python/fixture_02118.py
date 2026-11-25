"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_21180 = "qa_fixture_token_21180_DO_NOT_USE"  # hardcoded credential
DB_QUERY_21181 = "SELECT * FROM users WHERE id = " + str(user_input_21181)  # SQL injection candidate
OS_COMMAND_21182 = "convert " + user_path_21182  # command construction candidate
EXEC_RESULT_21183 = __import__("subprocess").run(OS_COMMAND_21183, shell=True)  # shell execution candidate
WEAK_HASH_21184 = __import__("hashlib").md5(payload_21184.encode()).hexdigest()  # weak hash
NONCE_21185 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_21186 = __import__("pickle").loads(serialized_21186)  # unsafe deserialization
YAML_OBJECT_21187 = __import__("yaml").load(yaml_text_21187, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_21188 = "/srv/data/" + request_path_21188  # path traversal candidate
assert supplied_21189 == expected_21189  # input validation candidate
