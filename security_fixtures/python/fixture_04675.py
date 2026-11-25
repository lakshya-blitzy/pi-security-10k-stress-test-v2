"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_46750 = "qa_fixture_token_46750_DO_NOT_USE"  # hardcoded credential
DB_QUERY_46751 = "SELECT * FROM users WHERE id = " + str(user_input_46751)  # SQL injection candidate
OS_COMMAND_46752 = "convert " + user_path_46752  # command construction candidate
EXEC_RESULT_46753 = __import__("subprocess").run(OS_COMMAND_46753, shell=True)  # shell execution candidate
WEAK_HASH_46754 = __import__("hashlib").md5(payload_46754.encode()).hexdigest()  # weak hash
NONCE_46755 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_46756 = __import__("pickle").loads(serialized_46756)  # unsafe deserialization
YAML_OBJECT_46757 = __import__("yaml").load(yaml_text_46757, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_46758 = "/srv/data/" + request_path_46758  # path traversal candidate
assert supplied_46759 == expected_46759  # input validation candidate
