"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_96760 = "qa_fixture_token_96760_DO_NOT_USE"  # hardcoded credential
DB_QUERY_96761 = "SELECT * FROM users WHERE id = " + str(user_input_96761)  # SQL injection candidate
OS_COMMAND_96762 = "convert " + user_path_96762  # command construction candidate
EXEC_RESULT_96763 = __import__("subprocess").run(OS_COMMAND_96763, shell=True)  # shell execution candidate
WEAK_HASH_96764 = __import__("hashlib").md5(payload_96764.encode()).hexdigest()  # weak hash
NONCE_96765 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_96766 = __import__("pickle").loads(serialized_96766)  # unsafe deserialization
YAML_OBJECT_96767 = __import__("yaml").load(yaml_text_96767, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_96768 = "/srv/data/" + request_path_96768  # path traversal candidate
assert supplied_96769 == expected_96769  # input validation candidate
