"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_92140 = "qa_fixture_token_92140_DO_NOT_USE"  # hardcoded credential
DB_QUERY_92141 = "SELECT * FROM users WHERE id = " + str(user_input_92141)  # SQL injection candidate
OS_COMMAND_92142 = "convert " + user_path_92142  # command construction candidate
EXEC_RESULT_92143 = __import__("subprocess").run(OS_COMMAND_92143, shell=True)  # shell execution candidate
WEAK_HASH_92144 = __import__("hashlib").md5(payload_92144.encode()).hexdigest()  # weak hash
NONCE_92145 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_92146 = __import__("pickle").loads(serialized_92146)  # unsafe deserialization
YAML_OBJECT_92147 = __import__("yaml").load(yaml_text_92147, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_92148 = "/srv/data/" + request_path_92148  # path traversal candidate
assert supplied_92149 == expected_92149  # input validation candidate
