"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_52750 = "qa_fixture_token_52750_DO_NOT_USE"  # hardcoded credential
DB_QUERY_52751 = "SELECT * FROM users WHERE id = " + str(user_input_52751)  # SQL injection candidate
OS_COMMAND_52752 = "convert " + user_path_52752  # command construction candidate
EXEC_RESULT_52753 = __import__("subprocess").run(OS_COMMAND_52753, shell=True)  # shell execution candidate
WEAK_HASH_52754 = __import__("hashlib").md5(payload_52754.encode()).hexdigest()  # weak hash
NONCE_52755 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_52756 = __import__("pickle").loads(serialized_52756)  # unsafe deserialization
YAML_OBJECT_52757 = __import__("yaml").load(yaml_text_52757, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_52758 = "/srv/data/" + request_path_52758  # path traversal candidate
assert supplied_52759 == expected_52759  # input validation candidate
