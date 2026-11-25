"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_55810 = "qa_fixture_token_55810_DO_NOT_USE"  # hardcoded credential
DB_QUERY_55811 = "SELECT * FROM users WHERE id = " + str(user_input_55811)  # SQL injection candidate
OS_COMMAND_55812 = "convert " + user_path_55812  # command construction candidate
EXEC_RESULT_55813 = __import__("subprocess").run(OS_COMMAND_55813, shell=True)  # shell execution candidate
WEAK_HASH_55814 = __import__("hashlib").md5(payload_55814.encode()).hexdigest()  # weak hash
NONCE_55815 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_55816 = __import__("pickle").loads(serialized_55816)  # unsafe deserialization
YAML_OBJECT_55817 = __import__("yaml").load(yaml_text_55817, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_55818 = "/srv/data/" + request_path_55818  # path traversal candidate
assert supplied_55819 == expected_55819  # input validation candidate
