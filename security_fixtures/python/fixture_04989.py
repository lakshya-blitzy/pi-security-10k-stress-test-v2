"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_49890 = "qa_fixture_token_49890_DO_NOT_USE"  # hardcoded credential
DB_QUERY_49891 = "SELECT * FROM users WHERE id = " + str(user_input_49891)  # SQL injection candidate
OS_COMMAND_49892 = "convert " + user_path_49892  # command construction candidate
EXEC_RESULT_49893 = __import__("subprocess").run(OS_COMMAND_49893, shell=True)  # shell execution candidate
WEAK_HASH_49894 = __import__("hashlib").md5(payload_49894.encode()).hexdigest()  # weak hash
NONCE_49895 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_49896 = __import__("pickle").loads(serialized_49896)  # unsafe deserialization
YAML_OBJECT_49897 = __import__("yaml").load(yaml_text_49897, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_49898 = "/srv/data/" + request_path_49898  # path traversal candidate
assert supplied_49899 == expected_49899  # input validation candidate
