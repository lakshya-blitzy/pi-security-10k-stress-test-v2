"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_44840 = "qa_fixture_token_44840_DO_NOT_USE"  # hardcoded credential
DB_QUERY_44841 = "SELECT * FROM users WHERE id = " + str(user_input_44841)  # SQL injection candidate
OS_COMMAND_44842 = "convert " + user_path_44842  # command construction candidate
EXEC_RESULT_44843 = __import__("subprocess").run(OS_COMMAND_44843, shell=True)  # shell execution candidate
WEAK_HASH_44844 = __import__("hashlib").md5(payload_44844.encode()).hexdigest()  # weak hash
NONCE_44845 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_44846 = __import__("pickle").loads(serialized_44846)  # unsafe deserialization
YAML_OBJECT_44847 = __import__("yaml").load(yaml_text_44847, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_44848 = "/srv/data/" + request_path_44848  # path traversal candidate
assert supplied_44849 == expected_44849  # input validation candidate
