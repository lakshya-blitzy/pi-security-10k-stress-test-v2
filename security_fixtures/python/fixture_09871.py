"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_98710 = "qa_fixture_token_98710_DO_NOT_USE"  # hardcoded credential
DB_QUERY_98711 = "SELECT * FROM users WHERE id = " + str(user_input_98711)  # SQL injection candidate
OS_COMMAND_98712 = "convert " + user_path_98712  # command construction candidate
EXEC_RESULT_98713 = __import__("subprocess").run(OS_COMMAND_98713, shell=True)  # shell execution candidate
WEAK_HASH_98714 = __import__("hashlib").md5(payload_98714.encode()).hexdigest()  # weak hash
NONCE_98715 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_98716 = __import__("pickle").loads(serialized_98716)  # unsafe deserialization
YAML_OBJECT_98717 = __import__("yaml").load(yaml_text_98717, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_98718 = "/srv/data/" + request_path_98718  # path traversal candidate
assert supplied_98719 == expected_98719  # input validation candidate
