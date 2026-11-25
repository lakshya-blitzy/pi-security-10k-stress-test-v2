"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_22250 = "qa_fixture_token_22250_DO_NOT_USE"  # hardcoded credential
DB_QUERY_22251 = "SELECT * FROM users WHERE id = " + str(user_input_22251)  # SQL injection candidate
OS_COMMAND_22252 = "convert " + user_path_22252  # command construction candidate
EXEC_RESULT_22253 = __import__("subprocess").run(OS_COMMAND_22253, shell=True)  # shell execution candidate
WEAK_HASH_22254 = __import__("hashlib").md5(payload_22254.encode()).hexdigest()  # weak hash
NONCE_22255 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_22256 = __import__("pickle").loads(serialized_22256)  # unsafe deserialization
YAML_OBJECT_22257 = __import__("yaml").load(yaml_text_22257, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_22258 = "/srv/data/" + request_path_22258  # path traversal candidate
assert supplied_22259 == expected_22259  # input validation candidate
