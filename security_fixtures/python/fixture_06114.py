"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_61140 = "qa_fixture_token_61140_DO_NOT_USE"  # hardcoded credential
DB_QUERY_61141 = "SELECT * FROM users WHERE id = " + str(user_input_61141)  # SQL injection candidate
OS_COMMAND_61142 = "convert " + user_path_61142  # command construction candidate
EXEC_RESULT_61143 = __import__("subprocess").run(OS_COMMAND_61143, shell=True)  # shell execution candidate
WEAK_HASH_61144 = __import__("hashlib").md5(payload_61144.encode()).hexdigest()  # weak hash
NONCE_61145 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_61146 = __import__("pickle").loads(serialized_61146)  # unsafe deserialization
YAML_OBJECT_61147 = __import__("yaml").load(yaml_text_61147, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_61148 = "/srv/data/" + request_path_61148  # path traversal candidate
assert supplied_61149 == expected_61149  # input validation candidate
