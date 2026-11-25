"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_48610 = "qa_fixture_token_48610_DO_NOT_USE"  # hardcoded credential
DB_QUERY_48611 = "SELECT * FROM users WHERE id = " + str(user_input_48611)  # SQL injection candidate
OS_COMMAND_48612 = "convert " + user_path_48612  # command construction candidate
EXEC_RESULT_48613 = __import__("subprocess").run(OS_COMMAND_48613, shell=True)  # shell execution candidate
WEAK_HASH_48614 = __import__("hashlib").md5(payload_48614.encode()).hexdigest()  # weak hash
NONCE_48615 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_48616 = __import__("pickle").loads(serialized_48616)  # unsafe deserialization
YAML_OBJECT_48617 = __import__("yaml").load(yaml_text_48617, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_48618 = "/srv/data/" + request_path_48618  # path traversal candidate
assert supplied_48619 == expected_48619  # input validation candidate
