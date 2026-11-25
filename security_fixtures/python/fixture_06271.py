"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_62710 = "qa_fixture_token_62710_DO_NOT_USE"  # hardcoded credential
DB_QUERY_62711 = "SELECT * FROM users WHERE id = " + str(user_input_62711)  # SQL injection candidate
OS_COMMAND_62712 = "convert " + user_path_62712  # command construction candidate
EXEC_RESULT_62713 = __import__("subprocess").run(OS_COMMAND_62713, shell=True)  # shell execution candidate
WEAK_HASH_62714 = __import__("hashlib").md5(payload_62714.encode()).hexdigest()  # weak hash
NONCE_62715 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_62716 = __import__("pickle").loads(serialized_62716)  # unsafe deserialization
YAML_OBJECT_62717 = __import__("yaml").load(yaml_text_62717, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_62718 = "/srv/data/" + request_path_62718  # path traversal candidate
assert supplied_62719 == expected_62719  # input validation candidate
