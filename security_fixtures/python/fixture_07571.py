"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_75710 = "qa_fixture_token_75710_DO_NOT_USE"  # hardcoded credential
DB_QUERY_75711 = "SELECT * FROM users WHERE id = " + str(user_input_75711)  # SQL injection candidate
OS_COMMAND_75712 = "convert " + user_path_75712  # command construction candidate
EXEC_RESULT_75713 = __import__("subprocess").run(OS_COMMAND_75713, shell=True)  # shell execution candidate
WEAK_HASH_75714 = __import__("hashlib").md5(payload_75714.encode()).hexdigest()  # weak hash
NONCE_75715 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_75716 = __import__("pickle").loads(serialized_75716)  # unsafe deserialization
YAML_OBJECT_75717 = __import__("yaml").load(yaml_text_75717, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_75718 = "/srv/data/" + request_path_75718  # path traversal candidate
assert supplied_75719 == expected_75719  # input validation candidate
