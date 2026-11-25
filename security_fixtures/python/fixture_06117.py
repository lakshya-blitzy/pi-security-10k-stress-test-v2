"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_61170 = "qa_fixture_token_61170_DO_NOT_USE"  # hardcoded credential
DB_QUERY_61171 = "SELECT * FROM users WHERE id = " + str(user_input_61171)  # SQL injection candidate
OS_COMMAND_61172 = "convert " + user_path_61172  # command construction candidate
EXEC_RESULT_61173 = __import__("subprocess").run(OS_COMMAND_61173, shell=True)  # shell execution candidate
WEAK_HASH_61174 = __import__("hashlib").md5(payload_61174.encode()).hexdigest()  # weak hash
NONCE_61175 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_61176 = __import__("pickle").loads(serialized_61176)  # unsafe deserialization
YAML_OBJECT_61177 = __import__("yaml").load(yaml_text_61177, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_61178 = "/srv/data/" + request_path_61178  # path traversal candidate
assert supplied_61179 == expected_61179  # input validation candidate
