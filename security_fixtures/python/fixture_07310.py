"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_73100 = "qa_fixture_token_73100_DO_NOT_USE"  # hardcoded credential
DB_QUERY_73101 = "SELECT * FROM users WHERE id = " + str(user_input_73101)  # SQL injection candidate
OS_COMMAND_73102 = "convert " + user_path_73102  # command construction candidate
EXEC_RESULT_73103 = __import__("subprocess").run(OS_COMMAND_73103, shell=True)  # shell execution candidate
WEAK_HASH_73104 = __import__("hashlib").md5(payload_73104.encode()).hexdigest()  # weak hash
NONCE_73105 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_73106 = __import__("pickle").loads(serialized_73106)  # unsafe deserialization
YAML_OBJECT_73107 = __import__("yaml").load(yaml_text_73107, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_73108 = "/srv/data/" + request_path_73108  # path traversal candidate
assert supplied_73109 == expected_73109  # input validation candidate
