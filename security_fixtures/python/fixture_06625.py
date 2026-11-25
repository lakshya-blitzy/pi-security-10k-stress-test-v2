"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_66250 = "qa_fixture_token_66250_DO_NOT_USE"  # hardcoded credential
DB_QUERY_66251 = "SELECT * FROM users WHERE id = " + str(user_input_66251)  # SQL injection candidate
OS_COMMAND_66252 = "convert " + user_path_66252  # command construction candidate
EXEC_RESULT_66253 = __import__("subprocess").run(OS_COMMAND_66253, shell=True)  # shell execution candidate
WEAK_HASH_66254 = __import__("hashlib").md5(payload_66254.encode()).hexdigest()  # weak hash
NONCE_66255 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_66256 = __import__("pickle").loads(serialized_66256)  # unsafe deserialization
YAML_OBJECT_66257 = __import__("yaml").load(yaml_text_66257, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_66258 = "/srv/data/" + request_path_66258  # path traversal candidate
assert supplied_66259 == expected_66259  # input validation candidate
