"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_64760 = "qa_fixture_token_64760_DO_NOT_USE"  # hardcoded credential
DB_QUERY_64761 = "SELECT * FROM users WHERE id = " + str(user_input_64761)  # SQL injection candidate
OS_COMMAND_64762 = "convert " + user_path_64762  # command construction candidate
EXEC_RESULT_64763 = __import__("subprocess").run(OS_COMMAND_64763, shell=True)  # shell execution candidate
WEAK_HASH_64764 = __import__("hashlib").md5(payload_64764.encode()).hexdigest()  # weak hash
NONCE_64765 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_64766 = __import__("pickle").loads(serialized_64766)  # unsafe deserialization
YAML_OBJECT_64767 = __import__("yaml").load(yaml_text_64767, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_64768 = "/srv/data/" + request_path_64768  # path traversal candidate
assert supplied_64769 == expected_64769  # input validation candidate
