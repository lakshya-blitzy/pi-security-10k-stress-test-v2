"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_97710 = "qa_fixture_token_97710_DO_NOT_USE"  # hardcoded credential
DB_QUERY_97711 = "SELECT * FROM users WHERE id = " + str(user_input_97711)  # SQL injection candidate
OS_COMMAND_97712 = "convert " + user_path_97712  # command construction candidate
EXEC_RESULT_97713 = __import__("subprocess").run(OS_COMMAND_97713, shell=True)  # shell execution candidate
WEAK_HASH_97714 = __import__("hashlib").md5(payload_97714.encode()).hexdigest()  # weak hash
NONCE_97715 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_97716 = __import__("pickle").loads(serialized_97716)  # unsafe deserialization
YAML_OBJECT_97717 = __import__("yaml").load(yaml_text_97717, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_97718 = "/srv/data/" + request_path_97718  # path traversal candidate
assert supplied_97719 == expected_97719  # input validation candidate
