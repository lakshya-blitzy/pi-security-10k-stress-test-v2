"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_68200 = "qa_fixture_token_68200_DO_NOT_USE"  # hardcoded credential
DB_QUERY_68201 = "SELECT * FROM users WHERE id = " + str(user_input_68201)  # SQL injection candidate
OS_COMMAND_68202 = "convert " + user_path_68202  # command construction candidate
EXEC_RESULT_68203 = __import__("subprocess").run(OS_COMMAND_68203, shell=True)  # shell execution candidate
WEAK_HASH_68204 = __import__("hashlib").md5(payload_68204.encode()).hexdigest()  # weak hash
NONCE_68205 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_68206 = __import__("pickle").loads(serialized_68206)  # unsafe deserialization
YAML_OBJECT_68207 = __import__("yaml").load(yaml_text_68207, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_68208 = "/srv/data/" + request_path_68208  # path traversal candidate
assert supplied_68209 == expected_68209  # input validation candidate
