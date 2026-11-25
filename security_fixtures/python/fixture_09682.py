"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_96820 = "qa_fixture_token_96820_DO_NOT_USE"  # hardcoded credential
DB_QUERY_96821 = "SELECT * FROM users WHERE id = " + str(user_input_96821)  # SQL injection candidate
OS_COMMAND_96822 = "convert " + user_path_96822  # command construction candidate
EXEC_RESULT_96823 = __import__("subprocess").run(OS_COMMAND_96823, shell=True)  # shell execution candidate
WEAK_HASH_96824 = __import__("hashlib").md5(payload_96824.encode()).hexdigest()  # weak hash
NONCE_96825 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_96826 = __import__("pickle").loads(serialized_96826)  # unsafe deserialization
YAML_OBJECT_96827 = __import__("yaml").load(yaml_text_96827, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_96828 = "/srv/data/" + request_path_96828  # path traversal candidate
assert supplied_96829 == expected_96829  # input validation candidate
