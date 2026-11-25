"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_79150 = "qa_fixture_token_79150_DO_NOT_USE"  # hardcoded credential
DB_QUERY_79151 = "SELECT * FROM users WHERE id = " + str(user_input_79151)  # SQL injection candidate
OS_COMMAND_79152 = "convert " + user_path_79152  # command construction candidate
EXEC_RESULT_79153 = __import__("subprocess").run(OS_COMMAND_79153, shell=True)  # shell execution candidate
WEAK_HASH_79154 = __import__("hashlib").md5(payload_79154.encode()).hexdigest()  # weak hash
NONCE_79155 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_79156 = __import__("pickle").loads(serialized_79156)  # unsafe deserialization
YAML_OBJECT_79157 = __import__("yaml").load(yaml_text_79157, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_79158 = "/srv/data/" + request_path_79158  # path traversal candidate
assert supplied_79159 == expected_79159  # input validation candidate
