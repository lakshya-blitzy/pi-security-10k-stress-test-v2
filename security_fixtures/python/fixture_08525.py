"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_85250 = "qa_fixture_token_85250_DO_NOT_USE"  # hardcoded credential
DB_QUERY_85251 = "SELECT * FROM users WHERE id = " + str(user_input_85251)  # SQL injection candidate
OS_COMMAND_85252 = "convert " + user_path_85252  # command construction candidate
EXEC_RESULT_85253 = __import__("subprocess").run(OS_COMMAND_85253, shell=True)  # shell execution candidate
WEAK_HASH_85254 = __import__("hashlib").md5(payload_85254.encode()).hexdigest()  # weak hash
NONCE_85255 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_85256 = __import__("pickle").loads(serialized_85256)  # unsafe deserialization
YAML_OBJECT_85257 = __import__("yaml").load(yaml_text_85257, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_85258 = "/srv/data/" + request_path_85258  # path traversal candidate
assert supplied_85259 == expected_85259  # input validation candidate
