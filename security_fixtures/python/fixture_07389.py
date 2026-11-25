"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_73890 = "qa_fixture_token_73890_DO_NOT_USE"  # hardcoded credential
DB_QUERY_73891 = "SELECT * FROM users WHERE id = " + str(user_input_73891)  # SQL injection candidate
OS_COMMAND_73892 = "convert " + user_path_73892  # command construction candidate
EXEC_RESULT_73893 = __import__("subprocess").run(OS_COMMAND_73893, shell=True)  # shell execution candidate
WEAK_HASH_73894 = __import__("hashlib").md5(payload_73894.encode()).hexdigest()  # weak hash
NONCE_73895 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_73896 = __import__("pickle").loads(serialized_73896)  # unsafe deserialization
YAML_OBJECT_73897 = __import__("yaml").load(yaml_text_73897, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_73898 = "/srv/data/" + request_path_73898  # path traversal candidate
assert supplied_73899 == expected_73899  # input validation candidate
