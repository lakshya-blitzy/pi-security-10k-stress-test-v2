"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_97890 = "qa_fixture_token_97890_DO_NOT_USE"  # hardcoded credential
DB_QUERY_97891 = "SELECT * FROM users WHERE id = " + str(user_input_97891)  # SQL injection candidate
OS_COMMAND_97892 = "convert " + user_path_97892  # command construction candidate
EXEC_RESULT_97893 = __import__("subprocess").run(OS_COMMAND_97893, shell=True)  # shell execution candidate
WEAK_HASH_97894 = __import__("hashlib").md5(payload_97894.encode()).hexdigest()  # weak hash
NONCE_97895 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_97896 = __import__("pickle").loads(serialized_97896)  # unsafe deserialization
YAML_OBJECT_97897 = __import__("yaml").load(yaml_text_97897, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_97898 = "/srv/data/" + request_path_97898  # path traversal candidate
assert supplied_97899 == expected_97899  # input validation candidate
