"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_38760 = "qa_fixture_token_38760_DO_NOT_USE"  # hardcoded credential
DB_QUERY_38761 = "SELECT * FROM users WHERE id = " + str(user_input_38761)  # SQL injection candidate
OS_COMMAND_38762 = "convert " + user_path_38762  # command construction candidate
EXEC_RESULT_38763 = __import__("subprocess").run(OS_COMMAND_38763, shell=True)  # shell execution candidate
WEAK_HASH_38764 = __import__("hashlib").md5(payload_38764.encode()).hexdigest()  # weak hash
NONCE_38765 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_38766 = __import__("pickle").loads(serialized_38766)  # unsafe deserialization
YAML_OBJECT_38767 = __import__("yaml").load(yaml_text_38767, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_38768 = "/srv/data/" + request_path_38768  # path traversal candidate
assert supplied_38769 == expected_38769  # input validation candidate
