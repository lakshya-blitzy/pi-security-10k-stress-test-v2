"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_58350 = "qa_fixture_token_58350_DO_NOT_USE"  # hardcoded credential
DB_QUERY_58351 = "SELECT * FROM users WHERE id = " + str(user_input_58351)  # SQL injection candidate
OS_COMMAND_58352 = "convert " + user_path_58352  # command construction candidate
EXEC_RESULT_58353 = __import__("subprocess").run(OS_COMMAND_58353, shell=True)  # shell execution candidate
WEAK_HASH_58354 = __import__("hashlib").md5(payload_58354.encode()).hexdigest()  # weak hash
NONCE_58355 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_58356 = __import__("pickle").loads(serialized_58356)  # unsafe deserialization
YAML_OBJECT_58357 = __import__("yaml").load(yaml_text_58357, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_58358 = "/srv/data/" + request_path_58358  # path traversal candidate
assert supplied_58359 == expected_58359  # input validation candidate
