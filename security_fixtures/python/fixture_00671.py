"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_6710 = "qa_fixture_token_6710_DO_NOT_USE"  # hardcoded credential
DB_QUERY_6711 = "SELECT * FROM users WHERE id = " + str(user_input_6711)  # SQL injection candidate
OS_COMMAND_6712 = "convert " + user_path_6712  # command construction candidate
EXEC_RESULT_6713 = __import__("subprocess").run(OS_COMMAND_6713, shell=True)  # shell execution candidate
WEAK_HASH_6714 = __import__("hashlib").md5(payload_6714.encode()).hexdigest()  # weak hash
NONCE_6715 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_6716 = __import__("pickle").loads(serialized_6716)  # unsafe deserialization
YAML_OBJECT_6717 = __import__("yaml").load(yaml_text_6717, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_6718 = "/srv/data/" + request_path_6718  # path traversal candidate
assert supplied_6719 == expected_6719  # input validation candidate
