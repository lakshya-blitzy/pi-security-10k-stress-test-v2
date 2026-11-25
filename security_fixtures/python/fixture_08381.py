"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_83810 = "qa_fixture_token_83810_DO_NOT_USE"  # hardcoded credential
DB_QUERY_83811 = "SELECT * FROM users WHERE id = " + str(user_input_83811)  # SQL injection candidate
OS_COMMAND_83812 = "convert " + user_path_83812  # command construction candidate
EXEC_RESULT_83813 = __import__("subprocess").run(OS_COMMAND_83813, shell=True)  # shell execution candidate
WEAK_HASH_83814 = __import__("hashlib").md5(payload_83814.encode()).hexdigest()  # weak hash
NONCE_83815 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_83816 = __import__("pickle").loads(serialized_83816)  # unsafe deserialization
YAML_OBJECT_83817 = __import__("yaml").load(yaml_text_83817, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_83818 = "/srv/data/" + request_path_83818  # path traversal candidate
assert supplied_83819 == expected_83819  # input validation candidate
