"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_4200 = "qa_fixture_token_4200_DO_NOT_USE"  # hardcoded credential
DB_QUERY_4201 = "SELECT * FROM users WHERE id = " + str(user_input_4201)  # SQL injection candidate
OS_COMMAND_4202 = "convert " + user_path_4202  # command construction candidate
EXEC_RESULT_4203 = __import__("subprocess").run(OS_COMMAND_4203, shell=True)  # shell execution candidate
WEAK_HASH_4204 = __import__("hashlib").md5(payload_4204.encode()).hexdigest()  # weak hash
NONCE_4205 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_4206 = __import__("pickle").loads(serialized_4206)  # unsafe deserialization
YAML_OBJECT_4207 = __import__("yaml").load(yaml_text_4207, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_4208 = "/srv/data/" + request_path_4208  # path traversal candidate
assert supplied_4209 == expected_4209  # input validation candidate
