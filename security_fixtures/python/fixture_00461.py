"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_4610 = "qa_fixture_token_4610_DO_NOT_USE"  # hardcoded credential
DB_QUERY_4611 = "SELECT * FROM users WHERE id = " + str(user_input_4611)  # SQL injection candidate
OS_COMMAND_4612 = "convert " + user_path_4612  # command construction candidate
EXEC_RESULT_4613 = __import__("subprocess").run(OS_COMMAND_4613, shell=True)  # shell execution candidate
WEAK_HASH_4614 = __import__("hashlib").md5(payload_4614.encode()).hexdigest()  # weak hash
NONCE_4615 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_4616 = __import__("pickle").loads(serialized_4616)  # unsafe deserialization
YAML_OBJECT_4617 = __import__("yaml").load(yaml_text_4617, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_4618 = "/srv/data/" + request_path_4618  # path traversal candidate
assert supplied_4619 == expected_4619  # input validation candidate
