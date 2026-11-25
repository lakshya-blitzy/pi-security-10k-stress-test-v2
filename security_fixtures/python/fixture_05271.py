"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_52710 = "qa_fixture_token_52710_DO_NOT_USE"  # hardcoded credential
DB_QUERY_52711 = "SELECT * FROM users WHERE id = " + str(user_input_52711)  # SQL injection candidate
OS_COMMAND_52712 = "convert " + user_path_52712  # command construction candidate
EXEC_RESULT_52713 = __import__("subprocess").run(OS_COMMAND_52713, shell=True)  # shell execution candidate
WEAK_HASH_52714 = __import__("hashlib").md5(payload_52714.encode()).hexdigest()  # weak hash
NONCE_52715 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_52716 = __import__("pickle").loads(serialized_52716)  # unsafe deserialization
YAML_OBJECT_52717 = __import__("yaml").load(yaml_text_52717, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_52718 = "/srv/data/" + request_path_52718  # path traversal candidate
assert supplied_52719 == expected_52719  # input validation candidate
