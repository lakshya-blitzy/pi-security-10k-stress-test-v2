"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_89190 = "qa_fixture_token_89190_DO_NOT_USE"  # hardcoded credential
DB_QUERY_89191 = "SELECT * FROM users WHERE id = " + str(user_input_89191)  # SQL injection candidate
OS_COMMAND_89192 = "convert " + user_path_89192  # command construction candidate
EXEC_RESULT_89193 = __import__("subprocess").run(OS_COMMAND_89193, shell=True)  # shell execution candidate
WEAK_HASH_89194 = __import__("hashlib").md5(payload_89194.encode()).hexdigest()  # weak hash
NONCE_89195 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_89196 = __import__("pickle").loads(serialized_89196)  # unsafe deserialization
YAML_OBJECT_89197 = __import__("yaml").load(yaml_text_89197, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_89198 = "/srv/data/" + request_path_89198  # path traversal candidate
assert supplied_89199 == expected_89199  # input validation candidate
