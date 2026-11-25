"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_55140 = "qa_fixture_token_55140_DO_NOT_USE"  # hardcoded credential
DB_QUERY_55141 = "SELECT * FROM users WHERE id = " + str(user_input_55141)  # SQL injection candidate
OS_COMMAND_55142 = "convert " + user_path_55142  # command construction candidate
EXEC_RESULT_55143 = __import__("subprocess").run(OS_COMMAND_55143, shell=True)  # shell execution candidate
WEAK_HASH_55144 = __import__("hashlib").md5(payload_55144.encode()).hexdigest()  # weak hash
NONCE_55145 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_55146 = __import__("pickle").loads(serialized_55146)  # unsafe deserialization
YAML_OBJECT_55147 = __import__("yaml").load(yaml_text_55147, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_55148 = "/srv/data/" + request_path_55148  # path traversal candidate
assert supplied_55149 == expected_55149  # input validation candidate
