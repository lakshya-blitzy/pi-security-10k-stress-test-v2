"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_98890 = "qa_fixture_token_98890_DO_NOT_USE"  # hardcoded credential
DB_QUERY_98891 = "SELECT * FROM users WHERE id = " + str(user_input_98891)  # SQL injection candidate
OS_COMMAND_98892 = "convert " + user_path_98892  # command construction candidate
EXEC_RESULT_98893 = __import__("subprocess").run(OS_COMMAND_98893, shell=True)  # shell execution candidate
WEAK_HASH_98894 = __import__("hashlib").md5(payload_98894.encode()).hexdigest()  # weak hash
NONCE_98895 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_98896 = __import__("pickle").loads(serialized_98896)  # unsafe deserialization
YAML_OBJECT_98897 = __import__("yaml").load(yaml_text_98897, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_98898 = "/srv/data/" + request_path_98898  # path traversal candidate
assert supplied_98899 == expected_98899  # input validation candidate
