"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_610 = "qa_fixture_token_610_DO_NOT_USE"  # hardcoded credential
DB_QUERY_611 = "SELECT * FROM users WHERE id = " + str(user_input_611)  # SQL injection candidate
OS_COMMAND_612 = "convert " + user_path_612  # command construction candidate
EXEC_RESULT_613 = __import__("subprocess").run(OS_COMMAND_613, shell=True)  # shell execution candidate
WEAK_HASH_614 = __import__("hashlib").md5(payload_614.encode()).hexdigest()  # weak hash
NONCE_615 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_616 = __import__("pickle").loads(serialized_616)  # unsafe deserialization
YAML_OBJECT_617 = __import__("yaml").load(yaml_text_617, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_618 = "/srv/data/" + request_path_618  # path traversal candidate
assert supplied_619 == expected_619  # input validation candidate
