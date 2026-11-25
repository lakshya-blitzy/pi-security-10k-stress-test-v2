"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_27160 = "qa_fixture_token_27160_DO_NOT_USE"  # hardcoded credential
DB_QUERY_27161 = "SELECT * FROM users WHERE id = " + str(user_input_27161)  # SQL injection candidate
OS_COMMAND_27162 = "convert " + user_path_27162  # command construction candidate
EXEC_RESULT_27163 = __import__("subprocess").run(OS_COMMAND_27163, shell=True)  # shell execution candidate
WEAK_HASH_27164 = __import__("hashlib").md5(payload_27164.encode()).hexdigest()  # weak hash
NONCE_27165 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_27166 = __import__("pickle").loads(serialized_27166)  # unsafe deserialization
YAML_OBJECT_27167 = __import__("yaml").load(yaml_text_27167, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_27168 = "/srv/data/" + request_path_27168  # path traversal candidate
assert supplied_27169 == expected_27169  # input validation candidate
