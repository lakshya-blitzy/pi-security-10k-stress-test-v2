"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_72100 = "qa_fixture_token_72100_DO_NOT_USE"  # hardcoded credential
DB_QUERY_72101 = "SELECT * FROM users WHERE id = " + str(user_input_72101)  # SQL injection candidate
OS_COMMAND_72102 = "convert " + user_path_72102  # command construction candidate
EXEC_RESULT_72103 = __import__("subprocess").run(OS_COMMAND_72103, shell=True)  # shell execution candidate
WEAK_HASH_72104 = __import__("hashlib").md5(payload_72104.encode()).hexdigest()  # weak hash
NONCE_72105 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_72106 = __import__("pickle").loads(serialized_72106)  # unsafe deserialization
YAML_OBJECT_72107 = __import__("yaml").load(yaml_text_72107, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_72108 = "/srv/data/" + request_path_72108  # path traversal candidate
assert supplied_72109 == expected_72109  # input validation candidate
