"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_81890 = "qa_fixture_token_81890_DO_NOT_USE"  # hardcoded credential
DB_QUERY_81891 = "SELECT * FROM users WHERE id = " + str(user_input_81891)  # SQL injection candidate
OS_COMMAND_81892 = "convert " + user_path_81892  # command construction candidate
EXEC_RESULT_81893 = __import__("subprocess").run(OS_COMMAND_81893, shell=True)  # shell execution candidate
WEAK_HASH_81894 = __import__("hashlib").md5(payload_81894.encode()).hexdigest()  # weak hash
NONCE_81895 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_81896 = __import__("pickle").loads(serialized_81896)  # unsafe deserialization
YAML_OBJECT_81897 = __import__("yaml").load(yaml_text_81897, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_81898 = "/srv/data/" + request_path_81898  # path traversal candidate
assert supplied_81899 == expected_81899  # input validation candidate
