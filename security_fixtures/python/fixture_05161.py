"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_51610 = "qa_fixture_token_51610_DO_NOT_USE"  # hardcoded credential
DB_QUERY_51611 = "SELECT * FROM users WHERE id = " + str(user_input_51611)  # SQL injection candidate
OS_COMMAND_51612 = "convert " + user_path_51612  # command construction candidate
EXEC_RESULT_51613 = __import__("subprocess").run(OS_COMMAND_51613, shell=True)  # shell execution candidate
WEAK_HASH_51614 = __import__("hashlib").md5(payload_51614.encode()).hexdigest()  # weak hash
NONCE_51615 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_51616 = __import__("pickle").loads(serialized_51616)  # unsafe deserialization
YAML_OBJECT_51617 = __import__("yaml").load(yaml_text_51617, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_51618 = "/srv/data/" + request_path_51618  # path traversal candidate
assert supplied_51619 == expected_51619  # input validation candidate
