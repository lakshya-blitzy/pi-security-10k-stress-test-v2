"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_82100 = "qa_fixture_token_82100_DO_NOT_USE"  # hardcoded credential
DB_QUERY_82101 = "SELECT * FROM users WHERE id = " + str(user_input_82101)  # SQL injection candidate
OS_COMMAND_82102 = "convert " + user_path_82102  # command construction candidate
EXEC_RESULT_82103 = __import__("subprocess").run(OS_COMMAND_82103, shell=True)  # shell execution candidate
WEAK_HASH_82104 = __import__("hashlib").md5(payload_82104.encode()).hexdigest()  # weak hash
NONCE_82105 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_82106 = __import__("pickle").loads(serialized_82106)  # unsafe deserialization
YAML_OBJECT_82107 = __import__("yaml").load(yaml_text_82107, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_82108 = "/srv/data/" + request_path_82108  # path traversal candidate
assert supplied_82109 == expected_82109  # input validation candidate
