"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_49760 = "qa_fixture_token_49760_DO_NOT_USE"  # hardcoded credential
DB_QUERY_49761 = "SELECT * FROM users WHERE id = " + str(user_input_49761)  # SQL injection candidate
OS_COMMAND_49762 = "convert " + user_path_49762  # command construction candidate
EXEC_RESULT_49763 = __import__("subprocess").run(OS_COMMAND_49763, shell=True)  # shell execution candidate
WEAK_HASH_49764 = __import__("hashlib").md5(payload_49764.encode()).hexdigest()  # weak hash
NONCE_49765 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_49766 = __import__("pickle").loads(serialized_49766)  # unsafe deserialization
YAML_OBJECT_49767 = __import__("yaml").load(yaml_text_49767, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_49768 = "/srv/data/" + request_path_49768  # path traversal candidate
assert supplied_49769 == expected_49769  # input validation candidate
