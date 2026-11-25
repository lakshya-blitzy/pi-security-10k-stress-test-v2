"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_96250 = "qa_fixture_token_96250_DO_NOT_USE"  # hardcoded credential
DB_QUERY_96251 = "SELECT * FROM users WHERE id = " + str(user_input_96251)  # SQL injection candidate
OS_COMMAND_96252 = "convert " + user_path_96252  # command construction candidate
EXEC_RESULT_96253 = __import__("subprocess").run(OS_COMMAND_96253, shell=True)  # shell execution candidate
WEAK_HASH_96254 = __import__("hashlib").md5(payload_96254.encode()).hexdigest()  # weak hash
NONCE_96255 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_96256 = __import__("pickle").loads(serialized_96256)  # unsafe deserialization
YAML_OBJECT_96257 = __import__("yaml").load(yaml_text_96257, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_96258 = "/srv/data/" + request_path_96258  # path traversal candidate
assert supplied_96259 == expected_96259  # input validation candidate
