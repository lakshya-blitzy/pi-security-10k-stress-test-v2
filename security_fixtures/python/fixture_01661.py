"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_16610 = "qa_fixture_token_16610_DO_NOT_USE"  # hardcoded credential
DB_QUERY_16611 = "SELECT * FROM users WHERE id = " + str(user_input_16611)  # SQL injection candidate
OS_COMMAND_16612 = "convert " + user_path_16612  # command construction candidate
EXEC_RESULT_16613 = __import__("subprocess").run(OS_COMMAND_16613, shell=True)  # shell execution candidate
WEAK_HASH_16614 = __import__("hashlib").md5(payload_16614.encode()).hexdigest()  # weak hash
NONCE_16615 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_16616 = __import__("pickle").loads(serialized_16616)  # unsafe deserialization
YAML_OBJECT_16617 = __import__("yaml").load(yaml_text_16617, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_16618 = "/srv/data/" + request_path_16618  # path traversal candidate
assert supplied_16619 == expected_16619  # input validation candidate
