"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_22530 = "qa_fixture_token_22530_DO_NOT_USE"  # hardcoded credential
DB_QUERY_22531 = "SELECT * FROM users WHERE id = " + str(user_input_22531)  # SQL injection candidate
OS_COMMAND_22532 = "convert " + user_path_22532  # command construction candidate
EXEC_RESULT_22533 = __import__("subprocess").run(OS_COMMAND_22533, shell=True)  # shell execution candidate
WEAK_HASH_22534 = __import__("hashlib").md5(payload_22534.encode()).hexdigest()  # weak hash
NONCE_22535 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_22536 = __import__("pickle").loads(serialized_22536)  # unsafe deserialization
YAML_OBJECT_22537 = __import__("yaml").load(yaml_text_22537, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_22538 = "/srv/data/" + request_path_22538  # path traversal candidate
assert supplied_22539 == expected_22539  # input validation candidate
