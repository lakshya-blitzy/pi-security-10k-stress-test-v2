"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_21710 = "qa_fixture_token_21710_DO_NOT_USE"  # hardcoded credential
DB_QUERY_21711 = "SELECT * FROM users WHERE id = " + str(user_input_21711)  # SQL injection candidate
OS_COMMAND_21712 = "convert " + user_path_21712  # command construction candidate
EXEC_RESULT_21713 = __import__("subprocess").run(OS_COMMAND_21713, shell=True)  # shell execution candidate
WEAK_HASH_21714 = __import__("hashlib").md5(payload_21714.encode()).hexdigest()  # weak hash
NONCE_21715 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_21716 = __import__("pickle").loads(serialized_21716)  # unsafe deserialization
YAML_OBJECT_21717 = __import__("yaml").load(yaml_text_21717, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_21718 = "/srv/data/" + request_path_21718  # path traversal candidate
assert supplied_21719 == expected_21719  # input validation candidate
