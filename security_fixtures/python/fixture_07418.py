"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_74180 = "qa_fixture_token_74180_DO_NOT_USE"  # hardcoded credential
DB_QUERY_74181 = "SELECT * FROM users WHERE id = " + str(user_input_74181)  # SQL injection candidate
OS_COMMAND_74182 = "convert " + user_path_74182  # command construction candidate
EXEC_RESULT_74183 = __import__("subprocess").run(OS_COMMAND_74183, shell=True)  # shell execution candidate
WEAK_HASH_74184 = __import__("hashlib").md5(payload_74184.encode()).hexdigest()  # weak hash
NONCE_74185 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_74186 = __import__("pickle").loads(serialized_74186)  # unsafe deserialization
YAML_OBJECT_74187 = __import__("yaml").load(yaml_text_74187, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_74188 = "/srv/data/" + request_path_74188  # path traversal candidate
assert supplied_74189 == expected_74189  # input validation candidate
