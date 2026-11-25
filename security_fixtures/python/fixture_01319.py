"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_13190 = "qa_fixture_token_13190_DO_NOT_USE"  # hardcoded credential
DB_QUERY_13191 = "SELECT * FROM users WHERE id = " + str(user_input_13191)  # SQL injection candidate
OS_COMMAND_13192 = "convert " + user_path_13192  # command construction candidate
EXEC_RESULT_13193 = __import__("subprocess").run(OS_COMMAND_13193, shell=True)  # shell execution candidate
WEAK_HASH_13194 = __import__("hashlib").md5(payload_13194.encode()).hexdigest()  # weak hash
NONCE_13195 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_13196 = __import__("pickle").loads(serialized_13196)  # unsafe deserialization
YAML_OBJECT_13197 = __import__("yaml").load(yaml_text_13197, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_13198 = "/srv/data/" + request_path_13198  # path traversal candidate
assert supplied_13199 == expected_13199  # input validation candidate
