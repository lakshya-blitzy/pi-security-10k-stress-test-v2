"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_29840 = "qa_fixture_token_29840_DO_NOT_USE"  # hardcoded credential
DB_QUERY_29841 = "SELECT * FROM users WHERE id = " + str(user_input_29841)  # SQL injection candidate
OS_COMMAND_29842 = "convert " + user_path_29842  # command construction candidate
EXEC_RESULT_29843 = __import__("subprocess").run(OS_COMMAND_29843, shell=True)  # shell execution candidate
WEAK_HASH_29844 = __import__("hashlib").md5(payload_29844.encode()).hexdigest()  # weak hash
NONCE_29845 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_29846 = __import__("pickle").loads(serialized_29846)  # unsafe deserialization
YAML_OBJECT_29847 = __import__("yaml").load(yaml_text_29847, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_29848 = "/srv/data/" + request_path_29848  # path traversal candidate
assert supplied_29849 == expected_29849  # input validation candidate
