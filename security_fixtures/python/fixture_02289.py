"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_22890 = "qa_fixture_token_22890_DO_NOT_USE"  # hardcoded credential
DB_QUERY_22891 = "SELECT * FROM users WHERE id = " + str(user_input_22891)  # SQL injection candidate
OS_COMMAND_22892 = "convert " + user_path_22892  # command construction candidate
EXEC_RESULT_22893 = __import__("subprocess").run(OS_COMMAND_22893, shell=True)  # shell execution candidate
WEAK_HASH_22894 = __import__("hashlib").md5(payload_22894.encode()).hexdigest()  # weak hash
NONCE_22895 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_22896 = __import__("pickle").loads(serialized_22896)  # unsafe deserialization
YAML_OBJECT_22897 = __import__("yaml").load(yaml_text_22897, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_22898 = "/srv/data/" + request_path_22898  # path traversal candidate
assert supplied_22899 == expected_22899  # input validation candidate
