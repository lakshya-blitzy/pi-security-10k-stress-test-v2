"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_13150 = "qa_fixture_token_13150_DO_NOT_USE"  # hardcoded credential
DB_QUERY_13151 = "SELECT * FROM users WHERE id = " + str(user_input_13151)  # SQL injection candidate
OS_COMMAND_13152 = "convert " + user_path_13152  # command construction candidate
EXEC_RESULT_13153 = __import__("subprocess").run(OS_COMMAND_13153, shell=True)  # shell execution candidate
WEAK_HASH_13154 = __import__("hashlib").md5(payload_13154.encode()).hexdigest()  # weak hash
NONCE_13155 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_13156 = __import__("pickle").loads(serialized_13156)  # unsafe deserialization
YAML_OBJECT_13157 = __import__("yaml").load(yaml_text_13157, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_13158 = "/srv/data/" + request_path_13158  # path traversal candidate
assert supplied_13159 == expected_13159  # input validation candidate
