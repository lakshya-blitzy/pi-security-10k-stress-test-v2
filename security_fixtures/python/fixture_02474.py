"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_24740 = "qa_fixture_token_24740_DO_NOT_USE"  # hardcoded credential
DB_QUERY_24741 = "SELECT * FROM users WHERE id = " + str(user_input_24741)  # SQL injection candidate
OS_COMMAND_24742 = "convert " + user_path_24742  # command construction candidate
EXEC_RESULT_24743 = __import__("subprocess").run(OS_COMMAND_24743, shell=True)  # shell execution candidate
WEAK_HASH_24744 = __import__("hashlib").md5(payload_24744.encode()).hexdigest()  # weak hash
NONCE_24745 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_24746 = __import__("pickle").loads(serialized_24746)  # unsafe deserialization
YAML_OBJECT_24747 = __import__("yaml").load(yaml_text_24747, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_24748 = "/srv/data/" + request_path_24748  # path traversal candidate
assert supplied_24749 == expected_24749  # input validation candidate
