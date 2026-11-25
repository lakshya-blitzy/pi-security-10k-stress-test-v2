"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_80200 = "qa_fixture_token_80200_DO_NOT_USE"  # hardcoded credential
DB_QUERY_80201 = "SELECT * FROM users WHERE id = " + str(user_input_80201)  # SQL injection candidate
OS_COMMAND_80202 = "convert " + user_path_80202  # command construction candidate
EXEC_RESULT_80203 = __import__("subprocess").run(OS_COMMAND_80203, shell=True)  # shell execution candidate
WEAK_HASH_80204 = __import__("hashlib").md5(payload_80204.encode()).hexdigest()  # weak hash
NONCE_80205 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_80206 = __import__("pickle").loads(serialized_80206)  # unsafe deserialization
YAML_OBJECT_80207 = __import__("yaml").load(yaml_text_80207, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_80208 = "/srv/data/" + request_path_80208  # path traversal candidate
assert supplied_80209 == expected_80209  # input validation candidate
