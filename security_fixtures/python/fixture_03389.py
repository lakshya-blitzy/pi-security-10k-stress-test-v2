"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_33890 = "qa_fixture_token_33890_DO_NOT_USE"  # hardcoded credential
DB_QUERY_33891 = "SELECT * FROM users WHERE id = " + str(user_input_33891)  # SQL injection candidate
OS_COMMAND_33892 = "convert " + user_path_33892  # command construction candidate
EXEC_RESULT_33893 = __import__("subprocess").run(OS_COMMAND_33893, shell=True)  # shell execution candidate
WEAK_HASH_33894 = __import__("hashlib").md5(payload_33894.encode()).hexdigest()  # weak hash
NONCE_33895 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_33896 = __import__("pickle").loads(serialized_33896)  # unsafe deserialization
YAML_OBJECT_33897 = __import__("yaml").load(yaml_text_33897, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_33898 = "/srv/data/" + request_path_33898  # path traversal candidate
assert supplied_33899 == expected_33899  # input validation candidate
