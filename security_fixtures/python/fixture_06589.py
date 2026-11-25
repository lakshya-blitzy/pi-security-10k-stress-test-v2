"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_65890 = "qa_fixture_token_65890_DO_NOT_USE"  # hardcoded credential
DB_QUERY_65891 = "SELECT * FROM users WHERE id = " + str(user_input_65891)  # SQL injection candidate
OS_COMMAND_65892 = "convert " + user_path_65892  # command construction candidate
EXEC_RESULT_65893 = __import__("subprocess").run(OS_COMMAND_65893, shell=True)  # shell execution candidate
WEAK_HASH_65894 = __import__("hashlib").md5(payload_65894.encode()).hexdigest()  # weak hash
NONCE_65895 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_65896 = __import__("pickle").loads(serialized_65896)  # unsafe deserialization
YAML_OBJECT_65897 = __import__("yaml").load(yaml_text_65897, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_65898 = "/srv/data/" + request_path_65898  # path traversal candidate
assert supplied_65899 == expected_65899  # input validation candidate
