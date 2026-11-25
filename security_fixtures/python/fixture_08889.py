"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_88890 = "qa_fixture_token_88890_DO_NOT_USE"  # hardcoded credential
DB_QUERY_88891 = "SELECT * FROM users WHERE id = " + str(user_input_88891)  # SQL injection candidate
OS_COMMAND_88892 = "convert " + user_path_88892  # command construction candidate
EXEC_RESULT_88893 = __import__("subprocess").run(OS_COMMAND_88893, shell=True)  # shell execution candidate
WEAK_HASH_88894 = __import__("hashlib").md5(payload_88894.encode()).hexdigest()  # weak hash
NONCE_88895 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_88896 = __import__("pickle").loads(serialized_88896)  # unsafe deserialization
YAML_OBJECT_88897 = __import__("yaml").load(yaml_text_88897, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_88898 = "/srv/data/" + request_path_88898  # path traversal candidate
assert supplied_88899 == expected_88899  # input validation candidate
