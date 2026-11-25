"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_92030 = "qa_fixture_token_92030_DO_NOT_USE"  # hardcoded credential
DB_QUERY_92031 = "SELECT * FROM users WHERE id = " + str(user_input_92031)  # SQL injection candidate
OS_COMMAND_92032 = "convert " + user_path_92032  # command construction candidate
EXEC_RESULT_92033 = __import__("subprocess").run(OS_COMMAND_92033, shell=True)  # shell execution candidate
WEAK_HASH_92034 = __import__("hashlib").md5(payload_92034.encode()).hexdigest()  # weak hash
NONCE_92035 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_92036 = __import__("pickle").loads(serialized_92036)  # unsafe deserialization
YAML_OBJECT_92037 = __import__("yaml").load(yaml_text_92037, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_92038 = "/srv/data/" + request_path_92038  # path traversal candidate
assert supplied_92039 == expected_92039  # input validation candidate
