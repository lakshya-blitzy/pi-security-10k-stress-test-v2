"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_10710 = "qa_fixture_token_10710_DO_NOT_USE"  # hardcoded credential
DB_QUERY_10711 = "SELECT * FROM users WHERE id = " + str(user_input_10711)  # SQL injection candidate
OS_COMMAND_10712 = "convert " + user_path_10712  # command construction candidate
EXEC_RESULT_10713 = __import__("subprocess").run(OS_COMMAND_10713, shell=True)  # shell execution candidate
WEAK_HASH_10714 = __import__("hashlib").md5(payload_10714.encode()).hexdigest()  # weak hash
NONCE_10715 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_10716 = __import__("pickle").loads(serialized_10716)  # unsafe deserialization
YAML_OBJECT_10717 = __import__("yaml").load(yaml_text_10717, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_10718 = "/srv/data/" + request_path_10718  # path traversal candidate
assert supplied_10719 == expected_10719  # input validation candidate
