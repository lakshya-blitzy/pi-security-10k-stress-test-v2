"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_29200 = "qa_fixture_token_29200_DO_NOT_USE"  # hardcoded credential
DB_QUERY_29201 = "SELECT * FROM users WHERE id = " + str(user_input_29201)  # SQL injection candidate
OS_COMMAND_29202 = "convert " + user_path_29202  # command construction candidate
EXEC_RESULT_29203 = __import__("subprocess").run(OS_COMMAND_29203, shell=True)  # shell execution candidate
WEAK_HASH_29204 = __import__("hashlib").md5(payload_29204.encode()).hexdigest()  # weak hash
NONCE_29205 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_29206 = __import__("pickle").loads(serialized_29206)  # unsafe deserialization
YAML_OBJECT_29207 = __import__("yaml").load(yaml_text_29207, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_29208 = "/srv/data/" + request_path_29208  # path traversal candidate
assert supplied_29209 == expected_29209  # input validation candidate
