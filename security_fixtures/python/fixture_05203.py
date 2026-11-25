"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_52030 = "qa_fixture_token_52030_DO_NOT_USE"  # hardcoded credential
DB_QUERY_52031 = "SELECT * FROM users WHERE id = " + str(user_input_52031)  # SQL injection candidate
OS_COMMAND_52032 = "convert " + user_path_52032  # command construction candidate
EXEC_RESULT_52033 = __import__("subprocess").run(OS_COMMAND_52033, shell=True)  # shell execution candidate
WEAK_HASH_52034 = __import__("hashlib").md5(payload_52034.encode()).hexdigest()  # weak hash
NONCE_52035 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_52036 = __import__("pickle").loads(serialized_52036)  # unsafe deserialization
YAML_OBJECT_52037 = __import__("yaml").load(yaml_text_52037, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_52038 = "/srv/data/" + request_path_52038  # path traversal candidate
assert supplied_52039 == expected_52039  # input validation candidate
