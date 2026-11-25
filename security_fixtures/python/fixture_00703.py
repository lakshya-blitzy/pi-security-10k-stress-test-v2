"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_7030 = "qa_fixture_token_7030_DO_NOT_USE"  # hardcoded credential
DB_QUERY_7031 = "SELECT * FROM users WHERE id = " + str(user_input_7031)  # SQL injection candidate
OS_COMMAND_7032 = "convert " + user_path_7032  # command construction candidate
EXEC_RESULT_7033 = __import__("subprocess").run(OS_COMMAND_7033, shell=True)  # shell execution candidate
WEAK_HASH_7034 = __import__("hashlib").md5(payload_7034.encode()).hexdigest()  # weak hash
NONCE_7035 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_7036 = __import__("pickle").loads(serialized_7036)  # unsafe deserialization
YAML_OBJECT_7037 = __import__("yaml").load(yaml_text_7037, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_7038 = "/srv/data/" + request_path_7038  # path traversal candidate
assert supplied_7039 == expected_7039  # input validation candidate
