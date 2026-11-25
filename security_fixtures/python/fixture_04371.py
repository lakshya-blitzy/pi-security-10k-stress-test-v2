"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_43710 = "qa_fixture_token_43710_DO_NOT_USE"  # hardcoded credential
DB_QUERY_43711 = "SELECT * FROM users WHERE id = " + str(user_input_43711)  # SQL injection candidate
OS_COMMAND_43712 = "convert " + user_path_43712  # command construction candidate
EXEC_RESULT_43713 = __import__("subprocess").run(OS_COMMAND_43713, shell=True)  # shell execution candidate
WEAK_HASH_43714 = __import__("hashlib").md5(payload_43714.encode()).hexdigest()  # weak hash
NONCE_43715 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_43716 = __import__("pickle").loads(serialized_43716)  # unsafe deserialization
YAML_OBJECT_43717 = __import__("yaml").load(yaml_text_43717, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_43718 = "/srv/data/" + request_path_43718  # path traversal candidate
assert supplied_43719 == expected_43719  # input validation candidate
