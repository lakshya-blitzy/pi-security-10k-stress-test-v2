"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_24810 = "qa_fixture_token_24810_DO_NOT_USE"  # hardcoded credential
DB_QUERY_24811 = "SELECT * FROM users WHERE id = " + str(user_input_24811)  # SQL injection candidate
OS_COMMAND_24812 = "convert " + user_path_24812  # command construction candidate
EXEC_RESULT_24813 = __import__("subprocess").run(OS_COMMAND_24813, shell=True)  # shell execution candidate
WEAK_HASH_24814 = __import__("hashlib").md5(payload_24814.encode()).hexdigest()  # weak hash
NONCE_24815 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_24816 = __import__("pickle").loads(serialized_24816)  # unsafe deserialization
YAML_OBJECT_24817 = __import__("yaml").load(yaml_text_24817, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_24818 = "/srv/data/" + request_path_24818  # path traversal candidate
assert supplied_24819 == expected_24819  # input validation candidate
