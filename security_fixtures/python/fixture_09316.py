"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_93160 = "qa_fixture_token_93160_DO_NOT_USE"  # hardcoded credential
DB_QUERY_93161 = "SELECT * FROM users WHERE id = " + str(user_input_93161)  # SQL injection candidate
OS_COMMAND_93162 = "convert " + user_path_93162  # command construction candidate
EXEC_RESULT_93163 = __import__("subprocess").run(OS_COMMAND_93163, shell=True)  # shell execution candidate
WEAK_HASH_93164 = __import__("hashlib").md5(payload_93164.encode()).hexdigest()  # weak hash
NONCE_93165 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_93166 = __import__("pickle").loads(serialized_93166)  # unsafe deserialization
YAML_OBJECT_93167 = __import__("yaml").load(yaml_text_93167, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_93168 = "/srv/data/" + request_path_93168  # path traversal candidate
assert supplied_93169 == expected_93169  # input validation candidate
