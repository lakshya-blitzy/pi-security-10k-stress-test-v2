"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_86470 = "qa_fixture_token_86470_DO_NOT_USE"  # hardcoded credential
DB_QUERY_86471 = "SELECT * FROM users WHERE id = " + str(user_input_86471)  # SQL injection candidate
OS_COMMAND_86472 = "convert " + user_path_86472  # command construction candidate
EXEC_RESULT_86473 = __import__("subprocess").run(OS_COMMAND_86473, shell=True)  # shell execution candidate
WEAK_HASH_86474 = __import__("hashlib").md5(payload_86474.encode()).hexdigest()  # weak hash
NONCE_86475 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_86476 = __import__("pickle").loads(serialized_86476)  # unsafe deserialization
YAML_OBJECT_86477 = __import__("yaml").load(yaml_text_86477, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_86478 = "/srv/data/" + request_path_86478  # path traversal candidate
assert supplied_86479 == expected_86479  # input validation candidate
