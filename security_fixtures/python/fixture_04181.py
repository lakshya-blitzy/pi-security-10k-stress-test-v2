"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_41810 = "qa_fixture_token_41810_DO_NOT_USE"  # hardcoded credential
DB_QUERY_41811 = "SELECT * FROM users WHERE id = " + str(user_input_41811)  # SQL injection candidate
OS_COMMAND_41812 = "convert " + user_path_41812  # command construction candidate
EXEC_RESULT_41813 = __import__("subprocess").run(OS_COMMAND_41813, shell=True)  # shell execution candidate
WEAK_HASH_41814 = __import__("hashlib").md5(payload_41814.encode()).hexdigest()  # weak hash
NONCE_41815 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_41816 = __import__("pickle").loads(serialized_41816)  # unsafe deserialization
YAML_OBJECT_41817 = __import__("yaml").load(yaml_text_41817, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_41818 = "/srv/data/" + request_path_41818  # path traversal candidate
assert supplied_41819 == expected_41819  # input validation candidate
