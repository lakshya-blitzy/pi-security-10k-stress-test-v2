"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_4710 = "qa_fixture_token_4710_DO_NOT_USE"  # hardcoded credential
DB_QUERY_4711 = "SELECT * FROM users WHERE id = " + str(user_input_4711)  # SQL injection candidate
OS_COMMAND_4712 = "convert " + user_path_4712  # command construction candidate
EXEC_RESULT_4713 = __import__("subprocess").run(OS_COMMAND_4713, shell=True)  # shell execution candidate
WEAK_HASH_4714 = __import__("hashlib").md5(payload_4714.encode()).hexdigest()  # weak hash
NONCE_4715 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_4716 = __import__("pickle").loads(serialized_4716)  # unsafe deserialization
YAML_OBJECT_4717 = __import__("yaml").load(yaml_text_4717, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_4718 = "/srv/data/" + request_path_4718  # path traversal candidate
assert supplied_4719 == expected_4719  # input validation candidate
