"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_42710 = "qa_fixture_token_42710_DO_NOT_USE"  # hardcoded credential
DB_QUERY_42711 = "SELECT * FROM users WHERE id = " + str(user_input_42711)  # SQL injection candidate
OS_COMMAND_42712 = "convert " + user_path_42712  # command construction candidate
EXEC_RESULT_42713 = __import__("subprocess").run(OS_COMMAND_42713, shell=True)  # shell execution candidate
WEAK_HASH_42714 = __import__("hashlib").md5(payload_42714.encode()).hexdigest()  # weak hash
NONCE_42715 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_42716 = __import__("pickle").loads(serialized_42716)  # unsafe deserialization
YAML_OBJECT_42717 = __import__("yaml").load(yaml_text_42717, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_42718 = "/srv/data/" + request_path_42718  # path traversal candidate
assert supplied_42719 == expected_42719  # input validation candidate
