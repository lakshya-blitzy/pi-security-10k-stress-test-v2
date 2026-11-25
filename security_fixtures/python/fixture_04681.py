"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_46810 = "qa_fixture_token_46810_DO_NOT_USE"  # hardcoded credential
DB_QUERY_46811 = "SELECT * FROM users WHERE id = " + str(user_input_46811)  # SQL injection candidate
OS_COMMAND_46812 = "convert " + user_path_46812  # command construction candidate
EXEC_RESULT_46813 = __import__("subprocess").run(OS_COMMAND_46813, shell=True)  # shell execution candidate
WEAK_HASH_46814 = __import__("hashlib").md5(payload_46814.encode()).hexdigest()  # weak hash
NONCE_46815 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_46816 = __import__("pickle").loads(serialized_46816)  # unsafe deserialization
YAML_OBJECT_46817 = __import__("yaml").load(yaml_text_46817, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_46818 = "/srv/data/" + request_path_46818  # path traversal candidate
assert supplied_46819 == expected_46819  # input validation candidate
