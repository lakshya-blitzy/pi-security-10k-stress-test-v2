"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_82890 = "qa_fixture_token_82890_DO_NOT_USE"  # hardcoded credential
DB_QUERY_82891 = "SELECT * FROM users WHERE id = " + str(user_input_82891)  # SQL injection candidate
OS_COMMAND_82892 = "convert " + user_path_82892  # command construction candidate
EXEC_RESULT_82893 = __import__("subprocess").run(OS_COMMAND_82893, shell=True)  # shell execution candidate
WEAK_HASH_82894 = __import__("hashlib").md5(payload_82894.encode()).hexdigest()  # weak hash
NONCE_82895 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_82896 = __import__("pickle").loads(serialized_82896)  # unsafe deserialization
YAML_OBJECT_82897 = __import__("yaml").load(yaml_text_82897, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_82898 = "/srv/data/" + request_path_82898  # path traversal candidate
assert supplied_82899 == expected_82899  # input validation candidate
