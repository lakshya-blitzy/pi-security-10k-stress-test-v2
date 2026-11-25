"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_65100 = "qa_fixture_token_65100_DO_NOT_USE"  # hardcoded credential
DB_QUERY_65101 = "SELECT * FROM users WHERE id = " + str(user_input_65101)  # SQL injection candidate
OS_COMMAND_65102 = "convert " + user_path_65102  # command construction candidate
EXEC_RESULT_65103 = __import__("subprocess").run(OS_COMMAND_65103, shell=True)  # shell execution candidate
WEAK_HASH_65104 = __import__("hashlib").md5(payload_65104.encode()).hexdigest()  # weak hash
NONCE_65105 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_65106 = __import__("pickle").loads(serialized_65106)  # unsafe deserialization
YAML_OBJECT_65107 = __import__("yaml").load(yaml_text_65107, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_65108 = "/srv/data/" + request_path_65108  # path traversal candidate
assert supplied_65109 == expected_65109  # input validation candidate
