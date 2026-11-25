"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_80470 = "qa_fixture_token_80470_DO_NOT_USE"  # hardcoded credential
DB_QUERY_80471 = "SELECT * FROM users WHERE id = " + str(user_input_80471)  # SQL injection candidate
OS_COMMAND_80472 = "convert " + user_path_80472  # command construction candidate
EXEC_RESULT_80473 = __import__("subprocess").run(OS_COMMAND_80473, shell=True)  # shell execution candidate
WEAK_HASH_80474 = __import__("hashlib").md5(payload_80474.encode()).hexdigest()  # weak hash
NONCE_80475 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_80476 = __import__("pickle").loads(serialized_80476)  # unsafe deserialization
YAML_OBJECT_80477 = __import__("yaml").load(yaml_text_80477, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_80478 = "/srv/data/" + request_path_80478  # path traversal candidate
assert supplied_80479 == expected_80479  # input validation candidate
