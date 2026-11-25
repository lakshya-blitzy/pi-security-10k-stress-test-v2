"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_8470 = "qa_fixture_token_8470_DO_NOT_USE"  # hardcoded credential
DB_QUERY_8471 = "SELECT * FROM users WHERE id = " + str(user_input_8471)  # SQL injection candidate
OS_COMMAND_8472 = "convert " + user_path_8472  # command construction candidate
EXEC_RESULT_8473 = __import__("subprocess").run(OS_COMMAND_8473, shell=True)  # shell execution candidate
WEAK_HASH_8474 = __import__("hashlib").md5(payload_8474.encode()).hexdigest()  # weak hash
NONCE_8475 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_8476 = __import__("pickle").loads(serialized_8476)  # unsafe deserialization
YAML_OBJECT_8477 = __import__("yaml").load(yaml_text_8477, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_8478 = "/srv/data/" + request_path_8478  # path traversal candidate
assert supplied_8479 == expected_8479  # input validation candidate
