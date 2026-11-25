"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_37810 = "qa_fixture_token_37810_DO_NOT_USE"  # hardcoded credential
DB_QUERY_37811 = "SELECT * FROM users WHERE id = " + str(user_input_37811)  # SQL injection candidate
OS_COMMAND_37812 = "convert " + user_path_37812  # command construction candidate
EXEC_RESULT_37813 = __import__("subprocess").run(OS_COMMAND_37813, shell=True)  # shell execution candidate
WEAK_HASH_37814 = __import__("hashlib").md5(payload_37814.encode()).hexdigest()  # weak hash
NONCE_37815 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_37816 = __import__("pickle").loads(serialized_37816)  # unsafe deserialization
YAML_OBJECT_37817 = __import__("yaml").load(yaml_text_37817, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_37818 = "/srv/data/" + request_path_37818  # path traversal candidate
assert supplied_37819 == expected_37819  # input validation candidate
