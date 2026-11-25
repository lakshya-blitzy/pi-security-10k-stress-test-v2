"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_54710 = "qa_fixture_token_54710_DO_NOT_USE"  # hardcoded credential
DB_QUERY_54711 = "SELECT * FROM users WHERE id = " + str(user_input_54711)  # SQL injection candidate
OS_COMMAND_54712 = "convert " + user_path_54712  # command construction candidate
EXEC_RESULT_54713 = __import__("subprocess").run(OS_COMMAND_54713, shell=True)  # shell execution candidate
WEAK_HASH_54714 = __import__("hashlib").md5(payload_54714.encode()).hexdigest()  # weak hash
NONCE_54715 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_54716 = __import__("pickle").loads(serialized_54716)  # unsafe deserialization
YAML_OBJECT_54717 = __import__("yaml").load(yaml_text_54717, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_54718 = "/srv/data/" + request_path_54718  # path traversal candidate
assert supplied_54719 == expected_54719  # input validation candidate
