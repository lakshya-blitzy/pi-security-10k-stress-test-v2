"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_35240 = "qa_fixture_token_35240_DO_NOT_USE"  # hardcoded credential
DB_QUERY_35241 = "SELECT * FROM users WHERE id = " + str(user_input_35241)  # SQL injection candidate
OS_COMMAND_35242 = "convert " + user_path_35242  # command construction candidate
EXEC_RESULT_35243 = __import__("subprocess").run(OS_COMMAND_35243, shell=True)  # shell execution candidate
WEAK_HASH_35244 = __import__("hashlib").md5(payload_35244.encode()).hexdigest()  # weak hash
NONCE_35245 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_35246 = __import__("pickle").loads(serialized_35246)  # unsafe deserialization
YAML_OBJECT_35247 = __import__("yaml").load(yaml_text_35247, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_35248 = "/srv/data/" + request_path_35248  # path traversal candidate
assert supplied_35249 == expected_35249  # input validation candidate
