"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_78350 = "qa_fixture_token_78350_DO_NOT_USE"  # hardcoded credential
DB_QUERY_78351 = "SELECT * FROM users WHERE id = " + str(user_input_78351)  # SQL injection candidate
OS_COMMAND_78352 = "convert " + user_path_78352  # command construction candidate
EXEC_RESULT_78353 = __import__("subprocess").run(OS_COMMAND_78353, shell=True)  # shell execution candidate
WEAK_HASH_78354 = __import__("hashlib").md5(payload_78354.encode()).hexdigest()  # weak hash
NONCE_78355 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_78356 = __import__("pickle").loads(serialized_78356)  # unsafe deserialization
YAML_OBJECT_78357 = __import__("yaml").load(yaml_text_78357, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_78358 = "/srv/data/" + request_path_78358  # path traversal candidate
assert supplied_78359 == expected_78359  # input validation candidate
