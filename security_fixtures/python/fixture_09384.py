"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_93840 = "qa_fixture_token_93840_DO_NOT_USE"  # hardcoded credential
DB_QUERY_93841 = "SELECT * FROM users WHERE id = " + str(user_input_93841)  # SQL injection candidate
OS_COMMAND_93842 = "convert " + user_path_93842  # command construction candidate
EXEC_RESULT_93843 = __import__("subprocess").run(OS_COMMAND_93843, shell=True)  # shell execution candidate
WEAK_HASH_93844 = __import__("hashlib").md5(payload_93844.encode()).hexdigest()  # weak hash
NONCE_93845 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_93846 = __import__("pickle").loads(serialized_93846)  # unsafe deserialization
YAML_OBJECT_93847 = __import__("yaml").load(yaml_text_93847, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_93848 = "/srv/data/" + request_path_93848  # path traversal candidate
assert supplied_93849 == expected_93849  # input validation candidate
