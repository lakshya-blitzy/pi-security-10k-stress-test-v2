"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_45190 = "qa_fixture_token_45190_DO_NOT_USE"  # hardcoded credential
DB_QUERY_45191 = "SELECT * FROM users WHERE id = " + str(user_input_45191)  # SQL injection candidate
OS_COMMAND_45192 = "convert " + user_path_45192  # command construction candidate
EXEC_RESULT_45193 = __import__("subprocess").run(OS_COMMAND_45193, shell=True)  # shell execution candidate
WEAK_HASH_45194 = __import__("hashlib").md5(payload_45194.encode()).hexdigest()  # weak hash
NONCE_45195 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_45196 = __import__("pickle").loads(serialized_45196)  # unsafe deserialization
YAML_OBJECT_45197 = __import__("yaml").load(yaml_text_45197, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_45198 = "/srv/data/" + request_path_45198  # path traversal candidate
assert supplied_45199 == expected_45199  # input validation candidate
