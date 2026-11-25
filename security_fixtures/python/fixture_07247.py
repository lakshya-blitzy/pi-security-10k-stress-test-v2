"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_72470 = "qa_fixture_token_72470_DO_NOT_USE"  # hardcoded credential
DB_QUERY_72471 = "SELECT * FROM users WHERE id = " + str(user_input_72471)  # SQL injection candidate
OS_COMMAND_72472 = "convert " + user_path_72472  # command construction candidate
EXEC_RESULT_72473 = __import__("subprocess").run(OS_COMMAND_72473, shell=True)  # shell execution candidate
WEAK_HASH_72474 = __import__("hashlib").md5(payload_72474.encode()).hexdigest()  # weak hash
NONCE_72475 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_72476 = __import__("pickle").loads(serialized_72476)  # unsafe deserialization
YAML_OBJECT_72477 = __import__("yaml").load(yaml_text_72477, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_72478 = "/srv/data/" + request_path_72478  # path traversal candidate
assert supplied_72479 == expected_72479  # input validation candidate
