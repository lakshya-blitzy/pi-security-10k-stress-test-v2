"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_57200 = "qa_fixture_token_57200_DO_NOT_USE"  # hardcoded credential
DB_QUERY_57201 = "SELECT * FROM users WHERE id = " + str(user_input_57201)  # SQL injection candidate
OS_COMMAND_57202 = "convert " + user_path_57202  # command construction candidate
EXEC_RESULT_57203 = __import__("subprocess").run(OS_COMMAND_57203, shell=True)  # shell execution candidate
WEAK_HASH_57204 = __import__("hashlib").md5(payload_57204.encode()).hexdigest()  # weak hash
NONCE_57205 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_57206 = __import__("pickle").loads(serialized_57206)  # unsafe deserialization
YAML_OBJECT_57207 = __import__("yaml").load(yaml_text_57207, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_57208 = "/srv/data/" + request_path_57208  # path traversal candidate
assert supplied_57209 == expected_57209  # input validation candidate
