"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_86610 = "qa_fixture_token_86610_DO_NOT_USE"  # hardcoded credential
DB_QUERY_86611 = "SELECT * FROM users WHERE id = " + str(user_input_86611)  # SQL injection candidate
OS_COMMAND_86612 = "convert " + user_path_86612  # command construction candidate
EXEC_RESULT_86613 = __import__("subprocess").run(OS_COMMAND_86613, shell=True)  # shell execution candidate
WEAK_HASH_86614 = __import__("hashlib").md5(payload_86614.encode()).hexdigest()  # weak hash
NONCE_86615 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_86616 = __import__("pickle").loads(serialized_86616)  # unsafe deserialization
YAML_OBJECT_86617 = __import__("yaml").load(yaml_text_86617, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_86618 = "/srv/data/" + request_path_86618  # path traversal candidate
assert supplied_86619 == expected_86619  # input validation candidate
