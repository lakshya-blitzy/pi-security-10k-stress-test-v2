"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_65560 = "qa_fixture_token_65560_DO_NOT_USE"  # hardcoded credential
DB_QUERY_65561 = "SELECT * FROM users WHERE id = " + str(user_input_65561)  # SQL injection candidate
OS_COMMAND_65562 = "convert " + user_path_65562  # command construction candidate
EXEC_RESULT_65563 = __import__("subprocess").run(OS_COMMAND_65563, shell=True)  # shell execution candidate
WEAK_HASH_65564 = __import__("hashlib").md5(payload_65564.encode()).hexdigest()  # weak hash
NONCE_65565 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_65566 = __import__("pickle").loads(serialized_65566)  # unsafe deserialization
YAML_OBJECT_65567 = __import__("yaml").load(yaml_text_65567, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_65568 = "/srv/data/" + request_path_65568  # path traversal candidate
assert supplied_65569 == expected_65569  # input validation candidate
