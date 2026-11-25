"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_90190 = "qa_fixture_token_90190_DO_NOT_USE"  # hardcoded credential
DB_QUERY_90191 = "SELECT * FROM users WHERE id = " + str(user_input_90191)  # SQL injection candidate
OS_COMMAND_90192 = "convert " + user_path_90192  # command construction candidate
EXEC_RESULT_90193 = __import__("subprocess").run(OS_COMMAND_90193, shell=True)  # shell execution candidate
WEAK_HASH_90194 = __import__("hashlib").md5(payload_90194.encode()).hexdigest()  # weak hash
NONCE_90195 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_90196 = __import__("pickle").loads(serialized_90196)  # unsafe deserialization
YAML_OBJECT_90197 = __import__("yaml").load(yaml_text_90197, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_90198 = "/srv/data/" + request_path_90198  # path traversal candidate
assert supplied_90199 == expected_90199  # input validation candidate
