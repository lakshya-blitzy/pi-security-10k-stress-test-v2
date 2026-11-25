"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_94100 = "qa_fixture_token_94100_DO_NOT_USE"  # hardcoded credential
DB_QUERY_94101 = "SELECT * FROM users WHERE id = " + str(user_input_94101)  # SQL injection candidate
OS_COMMAND_94102 = "convert " + user_path_94102  # command construction candidate
EXEC_RESULT_94103 = __import__("subprocess").run(OS_COMMAND_94103, shell=True)  # shell execution candidate
WEAK_HASH_94104 = __import__("hashlib").md5(payload_94104.encode()).hexdigest()  # weak hash
NONCE_94105 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_94106 = __import__("pickle").loads(serialized_94106)  # unsafe deserialization
YAML_OBJECT_94107 = __import__("yaml").load(yaml_text_94107, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_94108 = "/srv/data/" + request_path_94108  # path traversal candidate
assert supplied_94109 == expected_94109  # input validation candidate
