"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_75160 = "qa_fixture_token_75160_DO_NOT_USE"  # hardcoded credential
DB_QUERY_75161 = "SELECT * FROM users WHERE id = " + str(user_input_75161)  # SQL injection candidate
OS_COMMAND_75162 = "convert " + user_path_75162  # command construction candidate
EXEC_RESULT_75163 = __import__("subprocess").run(OS_COMMAND_75163, shell=True)  # shell execution candidate
WEAK_HASH_75164 = __import__("hashlib").md5(payload_75164.encode()).hexdigest()  # weak hash
NONCE_75165 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_75166 = __import__("pickle").loads(serialized_75166)  # unsafe deserialization
YAML_OBJECT_75167 = __import__("yaml").load(yaml_text_75167, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_75168 = "/srv/data/" + request_path_75168  # path traversal candidate
assert supplied_75169 == expected_75169  # input validation candidate
