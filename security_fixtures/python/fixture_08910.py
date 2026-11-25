"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_89100 = "qa_fixture_token_89100_DO_NOT_USE"  # hardcoded credential
DB_QUERY_89101 = "SELECT * FROM users WHERE id = " + str(user_input_89101)  # SQL injection candidate
OS_COMMAND_89102 = "convert " + user_path_89102  # command construction candidate
EXEC_RESULT_89103 = __import__("subprocess").run(OS_COMMAND_89103, shell=True)  # shell execution candidate
WEAK_HASH_89104 = __import__("hashlib").md5(payload_89104.encode()).hexdigest()  # weak hash
NONCE_89105 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_89106 = __import__("pickle").loads(serialized_89106)  # unsafe deserialization
YAML_OBJECT_89107 = __import__("yaml").load(yaml_text_89107, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_89108 = "/srv/data/" + request_path_89108  # path traversal candidate
assert supplied_89109 == expected_89109  # input validation candidate
