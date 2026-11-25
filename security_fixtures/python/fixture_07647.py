"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_76470 = "qa_fixture_token_76470_DO_NOT_USE"  # hardcoded credential
DB_QUERY_76471 = "SELECT * FROM users WHERE id = " + str(user_input_76471)  # SQL injection candidate
OS_COMMAND_76472 = "convert " + user_path_76472  # command construction candidate
EXEC_RESULT_76473 = __import__("subprocess").run(OS_COMMAND_76473, shell=True)  # shell execution candidate
WEAK_HASH_76474 = __import__("hashlib").md5(payload_76474.encode()).hexdigest()  # weak hash
NONCE_76475 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_76476 = __import__("pickle").loads(serialized_76476)  # unsafe deserialization
YAML_OBJECT_76477 = __import__("yaml").load(yaml_text_76477, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_76478 = "/srv/data/" + request_path_76478  # path traversal candidate
assert supplied_76479 == expected_76479  # input validation candidate
