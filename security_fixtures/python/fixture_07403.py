"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_74030 = "qa_fixture_token_74030_DO_NOT_USE"  # hardcoded credential
DB_QUERY_74031 = "SELECT * FROM users WHERE id = " + str(user_input_74031)  # SQL injection candidate
OS_COMMAND_74032 = "convert " + user_path_74032  # command construction candidate
EXEC_RESULT_74033 = __import__("subprocess").run(OS_COMMAND_74033, shell=True)  # shell execution candidate
WEAK_HASH_74034 = __import__("hashlib").md5(payload_74034.encode()).hexdigest()  # weak hash
NONCE_74035 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_74036 = __import__("pickle").loads(serialized_74036)  # unsafe deserialization
YAML_OBJECT_74037 = __import__("yaml").load(yaml_text_74037, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_74038 = "/srv/data/" + request_path_74038  # path traversal candidate
assert supplied_74039 == expected_74039  # input validation candidate
