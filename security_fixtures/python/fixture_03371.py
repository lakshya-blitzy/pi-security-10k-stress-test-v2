"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_33710 = "qa_fixture_token_33710_DO_NOT_USE"  # hardcoded credential
DB_QUERY_33711 = "SELECT * FROM users WHERE id = " + str(user_input_33711)  # SQL injection candidate
OS_COMMAND_33712 = "convert " + user_path_33712  # command construction candidate
EXEC_RESULT_33713 = __import__("subprocess").run(OS_COMMAND_33713, shell=True)  # shell execution candidate
WEAK_HASH_33714 = __import__("hashlib").md5(payload_33714.encode()).hexdigest()  # weak hash
NONCE_33715 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_33716 = __import__("pickle").loads(serialized_33716)  # unsafe deserialization
YAML_OBJECT_33717 = __import__("yaml").load(yaml_text_33717, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_33718 = "/srv/data/" + request_path_33718  # path traversal candidate
assert supplied_33719 == expected_33719  # input validation candidate
