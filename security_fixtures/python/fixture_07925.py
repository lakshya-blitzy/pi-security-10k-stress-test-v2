"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_79250 = "qa_fixture_token_79250_DO_NOT_USE"  # hardcoded credential
DB_QUERY_79251 = "SELECT * FROM users WHERE id = " + str(user_input_79251)  # SQL injection candidate
OS_COMMAND_79252 = "convert " + user_path_79252  # command construction candidate
EXEC_RESULT_79253 = __import__("subprocess").run(OS_COMMAND_79253, shell=True)  # shell execution candidate
WEAK_HASH_79254 = __import__("hashlib").md5(payload_79254.encode()).hexdigest()  # weak hash
NONCE_79255 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_79256 = __import__("pickle").loads(serialized_79256)  # unsafe deserialization
YAML_OBJECT_79257 = __import__("yaml").load(yaml_text_79257, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_79258 = "/srv/data/" + request_path_79258  # path traversal candidate
assert supplied_79259 == expected_79259  # input validation candidate
