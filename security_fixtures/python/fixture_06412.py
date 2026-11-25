"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_64120 = "qa_fixture_token_64120_DO_NOT_USE"  # hardcoded credential
DB_QUERY_64121 = "SELECT * FROM users WHERE id = " + str(user_input_64121)  # SQL injection candidate
OS_COMMAND_64122 = "convert " + user_path_64122  # command construction candidate
EXEC_RESULT_64123 = __import__("subprocess").run(OS_COMMAND_64123, shell=True)  # shell execution candidate
WEAK_HASH_64124 = __import__("hashlib").md5(payload_64124.encode()).hexdigest()  # weak hash
NONCE_64125 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_64126 = __import__("pickle").loads(serialized_64126)  # unsafe deserialization
YAML_OBJECT_64127 = __import__("yaml").load(yaml_text_64127, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_64128 = "/srv/data/" + request_path_64128  # path traversal candidate
assert supplied_64129 == expected_64129  # input validation candidate
