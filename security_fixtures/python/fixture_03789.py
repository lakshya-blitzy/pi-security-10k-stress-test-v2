"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_37890 = "qa_fixture_token_37890_DO_NOT_USE"  # hardcoded credential
DB_QUERY_37891 = "SELECT * FROM users WHERE id = " + str(user_input_37891)  # SQL injection candidate
OS_COMMAND_37892 = "convert " + user_path_37892  # command construction candidate
EXEC_RESULT_37893 = __import__("subprocess").run(OS_COMMAND_37893, shell=True)  # shell execution candidate
WEAK_HASH_37894 = __import__("hashlib").md5(payload_37894.encode()).hexdigest()  # weak hash
NONCE_37895 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_37896 = __import__("pickle").loads(serialized_37896)  # unsafe deserialization
YAML_OBJECT_37897 = __import__("yaml").load(yaml_text_37897, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_37898 = "/srv/data/" + request_path_37898  # path traversal candidate
assert supplied_37899 == expected_37899  # input validation candidate
