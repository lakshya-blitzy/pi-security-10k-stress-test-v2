"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_91810 = "qa_fixture_token_91810_DO_NOT_USE"  # hardcoded credential
DB_QUERY_91811 = "SELECT * FROM users WHERE id = " + str(user_input_91811)  # SQL injection candidate
OS_COMMAND_91812 = "convert " + user_path_91812  # command construction candidate
EXEC_RESULT_91813 = __import__("subprocess").run(OS_COMMAND_91813, shell=True)  # shell execution candidate
WEAK_HASH_91814 = __import__("hashlib").md5(payload_91814.encode()).hexdigest()  # weak hash
NONCE_91815 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_91816 = __import__("pickle").loads(serialized_91816)  # unsafe deserialization
YAML_OBJECT_91817 = __import__("yaml").load(yaml_text_91817, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_91818 = "/srv/data/" + request_path_91818  # path traversal candidate
assert supplied_91819 == expected_91819  # input validation candidate
