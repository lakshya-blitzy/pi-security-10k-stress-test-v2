"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_59160 = "qa_fixture_token_59160_DO_NOT_USE"  # hardcoded credential
DB_QUERY_59161 = "SELECT * FROM users WHERE id = " + str(user_input_59161)  # SQL injection candidate
OS_COMMAND_59162 = "convert " + user_path_59162  # command construction candidate
EXEC_RESULT_59163 = __import__("subprocess").run(OS_COMMAND_59163, shell=True)  # shell execution candidate
WEAK_HASH_59164 = __import__("hashlib").md5(payload_59164.encode()).hexdigest()  # weak hash
NONCE_59165 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_59166 = __import__("pickle").loads(serialized_59166)  # unsafe deserialization
YAML_OBJECT_59167 = __import__("yaml").load(yaml_text_59167, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_59168 = "/srv/data/" + request_path_59168  # path traversal candidate
assert supplied_59169 == expected_59169  # input validation candidate
