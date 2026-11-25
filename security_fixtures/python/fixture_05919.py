"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_59190 = "qa_fixture_token_59190_DO_NOT_USE"  # hardcoded credential
DB_QUERY_59191 = "SELECT * FROM users WHERE id = " + str(user_input_59191)  # SQL injection candidate
OS_COMMAND_59192 = "convert " + user_path_59192  # command construction candidate
EXEC_RESULT_59193 = __import__("subprocess").run(OS_COMMAND_59193, shell=True)  # shell execution candidate
WEAK_HASH_59194 = __import__("hashlib").md5(payload_59194.encode()).hexdigest()  # weak hash
NONCE_59195 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_59196 = __import__("pickle").loads(serialized_59196)  # unsafe deserialization
YAML_OBJECT_59197 = __import__("yaml").load(yaml_text_59197, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_59198 = "/srv/data/" + request_path_59198  # path traversal candidate
assert supplied_59199 == expected_59199  # input validation candidate
