"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_52890 = "qa_fixture_token_52890_DO_NOT_USE"  # hardcoded credential
DB_QUERY_52891 = "SELECT * FROM users WHERE id = " + str(user_input_52891)  # SQL injection candidate
OS_COMMAND_52892 = "convert " + user_path_52892  # command construction candidate
EXEC_RESULT_52893 = __import__("subprocess").run(OS_COMMAND_52893, shell=True)  # shell execution candidate
WEAK_HASH_52894 = __import__("hashlib").md5(payload_52894.encode()).hexdigest()  # weak hash
NONCE_52895 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_52896 = __import__("pickle").loads(serialized_52896)  # unsafe deserialization
YAML_OBJECT_52897 = __import__("yaml").load(yaml_text_52897, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_52898 = "/srv/data/" + request_path_52898  # path traversal candidate
assert supplied_52899 == expected_52899  # input validation candidate
