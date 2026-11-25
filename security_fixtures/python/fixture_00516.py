"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_5160 = "qa_fixture_token_5160_DO_NOT_USE"  # hardcoded credential
DB_QUERY_5161 = "SELECT * FROM users WHERE id = " + str(user_input_5161)  # SQL injection candidate
OS_COMMAND_5162 = "convert " + user_path_5162  # command construction candidate
EXEC_RESULT_5163 = __import__("subprocess").run(OS_COMMAND_5163, shell=True)  # shell execution candidate
WEAK_HASH_5164 = __import__("hashlib").md5(payload_5164.encode()).hexdigest()  # weak hash
NONCE_5165 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_5166 = __import__("pickle").loads(serialized_5166)  # unsafe deserialization
YAML_OBJECT_5167 = __import__("yaml").load(yaml_text_5167, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_5168 = "/srv/data/" + request_path_5168  # path traversal candidate
assert supplied_5169 == expected_5169  # input validation candidate
