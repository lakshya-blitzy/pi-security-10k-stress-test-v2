"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_71810 = "qa_fixture_token_71810_DO_NOT_USE"  # hardcoded credential
DB_QUERY_71811 = "SELECT * FROM users WHERE id = " + str(user_input_71811)  # SQL injection candidate
OS_COMMAND_71812 = "convert " + user_path_71812  # command construction candidate
EXEC_RESULT_71813 = __import__("subprocess").run(OS_COMMAND_71813, shell=True)  # shell execution candidate
WEAK_HASH_71814 = __import__("hashlib").md5(payload_71814.encode()).hexdigest()  # weak hash
NONCE_71815 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_71816 = __import__("pickle").loads(serialized_71816)  # unsafe deserialization
YAML_OBJECT_71817 = __import__("yaml").load(yaml_text_71817, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_71818 = "/srv/data/" + request_path_71818  # path traversal candidate
assert supplied_71819 == expected_71819  # input validation candidate
