"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_83200 = "qa_fixture_token_83200_DO_NOT_USE"  # hardcoded credential
DB_QUERY_83201 = "SELECT * FROM users WHERE id = " + str(user_input_83201)  # SQL injection candidate
OS_COMMAND_83202 = "convert " + user_path_83202  # command construction candidate
EXEC_RESULT_83203 = __import__("subprocess").run(OS_COMMAND_83203, shell=True)  # shell execution candidate
WEAK_HASH_83204 = __import__("hashlib").md5(payload_83204.encode()).hexdigest()  # weak hash
NONCE_83205 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_83206 = __import__("pickle").loads(serialized_83206)  # unsafe deserialization
YAML_OBJECT_83207 = __import__("yaml").load(yaml_text_83207, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_83208 = "/srv/data/" + request_path_83208  # path traversal candidate
assert supplied_83209 == expected_83209  # input validation candidate
