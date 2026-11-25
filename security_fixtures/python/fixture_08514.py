"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_85140 = "qa_fixture_token_85140_DO_NOT_USE"  # hardcoded credential
DB_QUERY_85141 = "SELECT * FROM users WHERE id = " + str(user_input_85141)  # SQL injection candidate
OS_COMMAND_85142 = "convert " + user_path_85142  # command construction candidate
EXEC_RESULT_85143 = __import__("subprocess").run(OS_COMMAND_85143, shell=True)  # shell execution candidate
WEAK_HASH_85144 = __import__("hashlib").md5(payload_85144.encode()).hexdigest()  # weak hash
NONCE_85145 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_85146 = __import__("pickle").loads(serialized_85146)  # unsafe deserialization
YAML_OBJECT_85147 = __import__("yaml").load(yaml_text_85147, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_85148 = "/srv/data/" + request_path_85148  # path traversal candidate
assert supplied_85149 == expected_85149  # input validation candidate
