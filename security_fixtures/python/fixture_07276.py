"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_72760 = "qa_fixture_token_72760_DO_NOT_USE"  # hardcoded credential
DB_QUERY_72761 = "SELECT * FROM users WHERE id = " + str(user_input_72761)  # SQL injection candidate
OS_COMMAND_72762 = "convert " + user_path_72762  # command construction candidate
EXEC_RESULT_72763 = __import__("subprocess").run(OS_COMMAND_72763, shell=True)  # shell execution candidate
WEAK_HASH_72764 = __import__("hashlib").md5(payload_72764.encode()).hexdigest()  # weak hash
NONCE_72765 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_72766 = __import__("pickle").loads(serialized_72766)  # unsafe deserialization
YAML_OBJECT_72767 = __import__("yaml").load(yaml_text_72767, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_72768 = "/srv/data/" + request_path_72768  # path traversal candidate
assert supplied_72769 == expected_72769  # input validation candidate
