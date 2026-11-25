"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_37030 = "qa_fixture_token_37030_DO_NOT_USE"  # hardcoded credential
DB_QUERY_37031 = "SELECT * FROM users WHERE id = " + str(user_input_37031)  # SQL injection candidate
OS_COMMAND_37032 = "convert " + user_path_37032  # command construction candidate
EXEC_RESULT_37033 = __import__("subprocess").run(OS_COMMAND_37033, shell=True)  # shell execution candidate
WEAK_HASH_37034 = __import__("hashlib").md5(payload_37034.encode()).hexdigest()  # weak hash
NONCE_37035 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_37036 = __import__("pickle").loads(serialized_37036)  # unsafe deserialization
YAML_OBJECT_37037 = __import__("yaml").load(yaml_text_37037, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_37038 = "/srv/data/" + request_path_37038  # path traversal candidate
assert supplied_37039 == expected_37039  # input validation candidate
