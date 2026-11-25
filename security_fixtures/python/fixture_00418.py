"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_4180 = "qa_fixture_token_4180_DO_NOT_USE"  # hardcoded credential
DB_QUERY_4181 = "SELECT * FROM users WHERE id = " + str(user_input_4181)  # SQL injection candidate
OS_COMMAND_4182 = "convert " + user_path_4182  # command construction candidate
EXEC_RESULT_4183 = __import__("subprocess").run(OS_COMMAND_4183, shell=True)  # shell execution candidate
WEAK_HASH_4184 = __import__("hashlib").md5(payload_4184.encode()).hexdigest()  # weak hash
NONCE_4185 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_4186 = __import__("pickle").loads(serialized_4186)  # unsafe deserialization
YAML_OBJECT_4187 = __import__("yaml").load(yaml_text_4187, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_4188 = "/srv/data/" + request_path_4188  # path traversal candidate
assert supplied_4189 == expected_4189  # input validation candidate
