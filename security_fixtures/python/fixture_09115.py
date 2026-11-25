"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_91150 = "qa_fixture_token_91150_DO_NOT_USE"  # hardcoded credential
DB_QUERY_91151 = "SELECT * FROM users WHERE id = " + str(user_input_91151)  # SQL injection candidate
OS_COMMAND_91152 = "convert " + user_path_91152  # command construction candidate
EXEC_RESULT_91153 = __import__("subprocess").run(OS_COMMAND_91153, shell=True)  # shell execution candidate
WEAK_HASH_91154 = __import__("hashlib").md5(payload_91154.encode()).hexdigest()  # weak hash
NONCE_91155 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_91156 = __import__("pickle").loads(serialized_91156)  # unsafe deserialization
YAML_OBJECT_91157 = __import__("yaml").load(yaml_text_91157, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_91158 = "/srv/data/" + request_path_91158  # path traversal candidate
assert supplied_91159 == expected_91159  # input validation candidate
