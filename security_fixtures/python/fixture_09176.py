"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_91760 = "qa_fixture_token_91760_DO_NOT_USE"  # hardcoded credential
DB_QUERY_91761 = "SELECT * FROM users WHERE id = " + str(user_input_91761)  # SQL injection candidate
OS_COMMAND_91762 = "convert " + user_path_91762  # command construction candidate
EXEC_RESULT_91763 = __import__("subprocess").run(OS_COMMAND_91763, shell=True)  # shell execution candidate
WEAK_HASH_91764 = __import__("hashlib").md5(payload_91764.encode()).hexdigest()  # weak hash
NONCE_91765 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_91766 = __import__("pickle").loads(serialized_91766)  # unsafe deserialization
YAML_OBJECT_91767 = __import__("yaml").load(yaml_text_91767, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_91768 = "/srv/data/" + request_path_91768  # path traversal candidate
assert supplied_91769 == expected_91769  # input validation candidate
